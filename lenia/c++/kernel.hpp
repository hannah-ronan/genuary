#pragma once

class Kernel {
	public:
		double kernelMax;
		int* mask;
		int* initialConfig;

		int* processImage(int* img, bool isMask);
};