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
distance = [[math.inf]*N for _ in range(N)]
for j in range(N):
    distance[j][j] = 0

for j in range(M):
    line = input()
    line = line.split()
    a = int(line[0])
    b = int(line[1])
    w = int(line[2])
    distance[a-1][b-1] = w

for k in range(N):
    for j in range(N):
        for i in range(N):
            distance[i][j] = min(distance[i][j], distance[i][k]+distance[k][j])
print(distance)