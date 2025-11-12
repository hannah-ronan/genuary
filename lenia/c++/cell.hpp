#pragma once
#include <vector>
#include "neighbour.hpp"  // include neighbour definition or forward declare if needed

class Cell {
public:
    int xCoord;
    int yCoord;
    double value;
    double prevValue = 0;
    std::vector<Neighbour> neighbours;

    double sumNeighbours();
};
