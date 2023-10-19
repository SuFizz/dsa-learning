#include <cassert>
#include <cstdint>
#include <iostream>
#include <vector>
using namespace std;

enum vertices { USD, EUR, GBP, CHF, CAD, MXN, INR };
uint32_t num_vertices = 7; // [O, A, B, C, D, E, T]
uint32_t num_relaxations = num_vertices - 1;
std::vector<std::vector<double>> edges = {
    {1, 0.741, 0.657, 1.061, 1.005, 19.023, 65.389},
    {1.349, 1, 0.888, 1.433, 1.366, 20.284, 70.125},
    {1.521, 1.126, 1, 1.614, 1.538, 23.613, 80.439},
    {0.942, 0.698, 0.619, 1, 0.953, 19.213, 65.445},
    {0.995, 0.732, 0.650, 1.049, 1, 14.442, 49.176},
    {0.052, 0.049, 0.042, 0.052, 0.069, 1, 3.402},
    {0.015, 0.014, 0.012, 0.015, 0.020, 0.294, 1}};
std::vector<double> distances;

bool relax_distances() {
  bool flag = false;
  if (distances[0] > 1)
    return false;
  for (uint32_t i = num_vertices - 1; i >= 0; --i) {
    //        std::cout << "\n i-" << i;
    for (uint32_t j = 0; j < num_vertices; ++j) {
      //            std::cout << " di-" << distances[i] << " ";
      if ((distances[i] != 0) && (distances[i] * edges[i][j] > distances[j])) {
        //                std::cout << " j-" << j << " " << distances[j];
        distances[j] = distances[i] * edges[i][j];
        flag = true;
      }
    }
    if (i == 0)
      return flag;
  }
  return flag;
}

int main() {
  distances.resize(num_vertices);
  for (auto &d : distances) {
    d = 0.0;
  }

  distances[USD] = 1; // traversing to T is the same as traversing from T
  for (uint32_t i = 0; i < num_relaxations; ++i) {
    if (!relax_distances())
      break;
  }
  for (uint32_t i = 0; i < num_vertices; ++i) {
    cout << "Distance from USD to " << i << " is " << distances[i] << endl;
  }
}