#pragma once
#include <vector>
#include "neighbour.hpp"  // include neighbour definition or forward declare if needed

class Cell {
public:
    double value = 0;
    double prevValue = 0;
    std::vector<Neighbour> neighbours;

    Cell();

    double sumNeighbours();
};
