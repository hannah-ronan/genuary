#pragma once
#include <opencv2/opencv.hpp>
#include <cmath>
#include <vector>
#include "cell.hpp"
#include "neighbour.hpp"

class Channel {
public:
    double kernelMax = 0;
    cv::Mat mask;
    cv::Mat initialConfig;
    double growthCentre;
    double growthRange;
    double deltaT;
    int width;
    int height;
    std::vector<std::vector<Cell>> cells;

    Channel(cv::Mat mask, cv::Mat initialConfig, double growthCentre, double growthRange, double deltaT);

    double getKernelMax(cv::Mat maskImg);

    void initCells();

    double growthFunc(Cell cell);

    void step();

    double clamp(double value, int min_val, int max_val);
};