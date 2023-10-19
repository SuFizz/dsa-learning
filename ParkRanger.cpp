#include <cassert>
#include <cstdint>
#include <iostream>
#include <vector>

enum vertices { O = 0, A, B, C, D, E, T };
uint32_t num_vertices = 7; // [O, A, B, C, D, E, T]
uint32_t num_relaxations = num_vertices - 1;
std::vector<std::vector<uint32_t>> edges;
std::vector<uint32_t> distances;

void input_vertices_and_edges() {
  edges.resize(num_vertices);
  for (auto &e : edges) {
    e.resize(num_vertices);
    for (auto &ei : e) {
      ei = -1; //   uint32 will initialize this to max
    }
  }
  edges[O][A] = 2;
  edges[O][B] = 5;
  edges[O][C] = 4;
  edges[A][O] = 2;
  edges[A][B] = 2;
  edges[A][D] = 7;
  edges[B][O] = 5;
  edges[B][A] = 2;
  edges[B][C] = 1;
  edges[B][D] = 4;
  edges[B][E] = 3;
  edges[C][O] = 4;
  edges[C][B] = 1;
  edges[C][E] = 4;
  edges[D][A] = 7;
  edges[D][B] = 4;
  edges[D][E] = 1;
  edges[D][T] = 5;
  edges[E][B] = 3;
  edges[E][C] = 4;
  edges[E][D] = 1;
  edges[E][T] = 7;
  edges[T][D] = 5;
  edges[T][E] = 7;

  for (int i = 0; i < num_vertices; ++i) {
    edges[i][i] = 0;
    for (int j = i + 1; j < num_vertices; ++j) {
      //            std::cout << edges[i][j] << " ";
      assert(edges[i][j] == edges[j][i]);
    }
    //        std::cout << std::endl;
  }
  distances.resize(num_vertices);
  for (auto &d : distances) {
    d = -1;
  }
}

bool relax_distances() {
  bool flag = false;
  for (uint32_t i = 0; i < num_vertices; ++i) {
    //        std::cout << "\n i-" << i;
    for (uint32_t j = 0; j < num_vertices; ++j) {
      //            std::cout << " di-" << distances[i] << " ";
      if ((edges[i][j] != -1) && (distances[i] != -1) &&
          ((distances[i] + edges[i][j] < distances[j]) || distances[j] == -1)) {
        //                std::cout << " j-" << j << " " << distances[j];
        distances[j] = distances[i] + edges[i][j];
        flag = true;
      }
    }
  }
  return flag;
}

int main() {
  input_vertices_and_edges();
  distances[T] = 0; // traversing to T is the same as traversing from T
  for (uint32_t i = 0; i < num_relaxations; ++i) {
    if (!relax_distances())
      break;
  }
  for (uint32_t i = 0; i < num_vertices; ++i) {
    std::cout << "Distance from T to " << i << " is " << distances[i]
              << std::endl;
  }
  // resetting distances
  for (auto &d : distances) {
    d = -1;
  }
  distances[O] = 0;

  for (uint32_t i = 0; i < num_relaxations; ++i) {
    if (!relax_distances())
      break;
  }
  for (uint32_t i = 0; i < num_vertices; ++i) {
    std::cout << "Distance from O to " << i << " is " << distances[i]
              << std::endl;
  }
}