#include <opencv2/opencv.hpp>
#include <cmath>
#include <vector>
#include <iostream>
#include "cell.hpp"
#include "neighbour.hpp"
#include "channel.hpp"

static const double expNeg1 = std::exp(-1.0);

Channel::Channel(cv::Mat _mask, cv::Mat _initialConfig, double _growthCentre, double _growthRange, double _deltaT) {
    mask = _mask;
    initialConfig = _initialConfig;
    growthCentre = _growthCentre;
    growthRange = _growthRange;
    deltaT = _deltaT;
    width = initialConfig.cols;
    height = initialConfig.rows;
    kernelMax = getKernelMax(mask);
    cells = std::vector<std::vector<Cell>>(height, std::vector<Cell>(width, Cell()));
    initCells();
}

double Channel::getKernelMax(cv::Mat maskImg) {
    std::cout << "\ncalculating kernel max...";
    double max = 0;
    for (int y = 0; y < maskImg.rows; y++) {
        for (int x = 0; x < maskImg.cols; x++) {
            double p = maskImg.at<uchar>(y, x);
            p = p / 255;
            max += p;
        }
    }
    std::cout << "\nkernal max: " << max;
    return max;
}

void Channel::initCells() {
    std::cout << "\ninitializing cells...";
    int maskMidpoint = ceil(double(mask.cols) / 2);
    //iterate over cells
    for (int y = 0; y < initialConfig.rows; y++) {
        for (int x = 0; x < initialConfig.cols; x++) {
            //set cell value based on initial config
            int cellValue = initialConfig.at<uchar>(y, x) / 255;
            cells[y][x].value = cellValue;

            //add cell neighbours
            for (int y_offset = 0; y_offset < mask.rows; y_offset++) {
                for (int x_offset = 0; x_offset < mask.cols; x_offset++) {
                    double maskValue = mask.at<uchar>(y_offset, x_offset) / 255;
                    if (maskValue > 0) { //only add the neighbour if weight is non-zero
                        try {
                            int neighbour_x = x - maskMidpoint + x_offset;
                            int neighbour_y = y - maskMidpoint + y_offset;
                            if (neighbour_y >= 0 && neighbour_x >= 0 && !(neighbour_x == x && neighbour_y == y)) { //don't check any negative indices, or the current cell
                                bool isProcessedBeforeParent = y_offset < maskMidpoint || (x_offset < maskMidpoint && y_offset < maskMidpoint);
                                Cell relative_cell = cells[neighbour_y][neighbour_x];
                                Neighbour new_neighbour = Neighbour(&relative_cell, maskValue, isProcessedBeforeParent);
                                cells[y][x].neighbours.push_back(new_neighbour);
                            }
                        }
                        catch (const std::runtime_error& e) {
                            std::cerr << "Runtime error: " << e.what() << std::endl;
                        }
                    }
                }
            }
        }
    }
}

double Channel::growthFunc(Cell cell) {
    double cell_neighbour_sum = cell.sumNeighbours();
    double normalized_sum = cell_neighbour_sum / kernelMax;
    if (abs(normalized_sum - growthCentre) < growthRange) {
        double x = (normalized_sum - growthCentre) / growthRange;
        double f = exp(-1 / (1 - pow(x, 2))) / expNeg1;
        return f - 0.5;
    }
    else{
        return -0.5;
    }
}

void Channel::step() {
    std::cout << "\nrunning step...";
    for (int y = 0; y < height; y++) {
        for (int x = 0; x < width; x++) {
            cells[y][x].prevValue = cells[y][x].value;
            double growth = growthFunc(cells[y][x]);
            growth = growth * deltaT;
            cells[y][x].value = clamp(cells[y][x].value + growth, 0, 1);
            double color = cells[y][x].value * 255;
            initialConfig.at<uchar>(y, x) = color;
        }
    }
    cv::imshow("step", initialConfig);
    cv::waitKey(10);
}

double Channel::clamp(double value, int min_val, int max_val) {
    if (value < min_val) {
        return min_val;
    }
    else if (value > max_val) {
        return max_val;
    }
    else {
        return value;
    }
}