#include "cell.hpp"

double Cell::sumNeighbours() {
    double neighbour_sum = 0;
    for (size_t i = 0; i < neighbours.size(); i++) {
        if (neighbours[i].isProcessedBeforeParent) {
            neighbour_sum += neighbours[i].cell->prevValue * neighbours[i].weight;
        }
        else {
            neighbour_sum += neighbours[i].cell->value * neighbours[i].weight;
        }
    }
    return neighbour_sum;
}
