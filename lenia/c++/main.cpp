#include <opencv2/opencv.hpp>
#include <iostream>
#include <string>
#include <chrono>
#include "channel.hpp"

std::string maskFilePath = "C:/Users/hanna/OneDrive/Documents/Programming_Projects/genuary/lenia/masks/radial.png";
std::string initialConfigFilePath = "C:/Users/hanna/OneDrive/Documents/Programming_Projects/genuary/lenia/initial_configs/plswork.png";
std::string outputFolder = "C:/Users/hanna/OneDrive/Documents/Programming_Projects/genuary/lenia/output_frames/";
int steps = 200;

int main() {
    cv::Mat maskImg = cv::imread(maskFilePath, cv::IMREAD_GRAYSCALE);
    cv::Mat initialConfigImg = cv::imread(initialConfigFilePath, cv::IMREAD_GRAYSCALE);

    if (maskImg.empty()) {
        std::cerr << "Failed to load mask image!\n";
        return 1;
    }

    if (initialConfigImg.empty()) {
        std::cerr << "Failed to load initial config image!\n";
        return 1;
    }
    
    Channel channel = Channel(maskImg, initialConfigImg, 0.5, 0.4, 0.1);
    

    auto start = std::chrono::high_resolution_clock::now();
    
    for (int i = 0; i < steps; i++) {
        channel.step();
        std::ostringstream filename;
        filename << outputFolder << "frame_" << i << ".png";
        cv::imwrite(filename.str(), initialConfigImg);
        cv::imshow("step", initialConfigImg);
        cv::waitKey(10);
    }

    auto end = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double> duration = end - start;
    std::cout << "\nexecution time is approximately " << duration.count() / steps << " seconds per step" << std::endl;

    return 0;
}