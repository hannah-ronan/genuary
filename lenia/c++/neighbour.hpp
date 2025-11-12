#pragma once

class Cell;

class Neighbour {
public:
    double weight;
    Cell* cell;
    bool isProcessedBeforeParent;
    Neighbour(Cell* _cell, double _weight, bool _isProcessedBeforeParent);
};
