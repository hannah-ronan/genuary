#include <opencv2/opencv.hpp>
#include <iostream>

int main() {
    cv::Mat img = cv::imread("test.png", cv::IMREAD_GRAYSCALE);
    if (img.empty()) {
        std::cerr << "Failed to load image!\n";
        return 1;
    }
    std::cout << "Image size: " << img.cols << " x " << img.rows << std::endl;
    return 0;
}