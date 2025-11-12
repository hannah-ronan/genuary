#include <vector>
//
//class Kernel{
//    public:
//        double kernelMax = 0;
//        int *mask;
//        int *initialConfig;
//
//        int* processImage(int *img, bool isMask){
//            int width, height = img.size;
//            std::vector<std::vector<int>> grid(height, std::vector<int>(width));
//            pixels = img.getdata();
//            for(int y = 0; y < height; y++){
//                for(int x = 0; x < width; x++){
//                    int idx = x + (y*width);
//                    int p = pixels[idx][0];
//                    p = map_value(p, (0,255), (0,1));
//                    if(isMask){
//                        kernelMax += p;
//                    }
//                    grid[y][x] = p;
//                }
//            }
//            return grid;
//        }
//};