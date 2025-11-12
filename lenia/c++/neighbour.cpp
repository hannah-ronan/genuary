#include "neighbour.hpp"

Neighbour::Neighbour(Cell* _cell, double _weight, bool _isProcessedBeforeParent) {
    cell = _cell;
    weight = _weight;
    isProcessedBeforeParent = _isProcessedBeforeParent;
}