#pragma once

class Cell;

class Neighbour {
public:
    double weight;
    Cell* cell;
    bool isProcessedBeforeParent;
};
