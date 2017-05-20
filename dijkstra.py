# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import math
import heapq

class edge:
    def __init__(self,a,b,w):
        self.a = a
        self.b = b
        self.w = w

class vertex:
    def __init__(self,index):
        self.index = index
        self.weights = {}
        self.visited = 0
    def weight(self,b,w):
        self.weights[b] = w

line1 = input()
N=int(line1.split()[0])
M=int(line1.split()[1])

vertices = []

edges = []
vertices = [vertex(i) for i in range(N)]
distance = [math.inf]*N
distance[0] = 0

for j in range(M):
    line = input()
    line = line.split()
    a = int(line[0])
    b = int(line[1])
    w = int(line[2])
    edges.append(edge(a,b,w))
    vertices[a-1].weight(b,w)


for _ in range(N):
    min_dist = heapq.nsmallest(len([i for i in distance if i<math.inf]), ((k,j) for j,k in enumerate(distance)))
    for q in range(len(distance)):
        min_dist_q = min_dist[q]
        min_dist_val = min_dist_q[0]
        min_dist_idx = min_dist_q[1]
        #print (min_dist_q)
        if(not(vertices[min_dist_idx].visited)):
            break
    vertices[min_dist_idx].visited = 1
    for ed in vertices[min_dist_idx].weights:
        distance[ed-1] = ( distance[min_dist_idx] + vertices[min_dist_idx].weights[ed] ) if (distance[min_dist_idx] + vertices[min_dist_idx].weights[ed] < distance[ed-1]) else distance[ed-1]

print(distance)