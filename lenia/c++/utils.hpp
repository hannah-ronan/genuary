#pragma once
inline double mapValue(double value, double srcStart, double srcEnd, double dstStart, double dstEnd){
    return ((value - srcStart) / (srcEnd-srcStart)) * (dstEnd-dstStart) + dstStart;
}
