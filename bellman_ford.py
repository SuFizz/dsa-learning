# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import math

class edge:
    def __init__(self,a,b,w):
        self.a = a
        self.b = b
        self.w = w

class vertex:
    def __init__(self,index,N):
        self.index = index
        self.weights = [math.inf]*N
        self.visited = 0
    def weight(self,b,w):
        self.weights[b-1] = w


line1 = input()
N=int(line1.split()[0])
M=int(line1.split()[1])

edges = []
distance = [math.inf]*N
distance[0] = 0
           
for j in range(M):
    line = input()
    line = line.split()
    a = int(line[0])
    b = int(line[1])
    w = int(line[2])
    edges.append(edge(a,b,w))

for i in range(N-1):
    flag = 0
    for edg in edges:
        (distance[edg.b-1],flag) = ((distance[edg.a-1] + edg.w),1) if (distance[edg.b-1] > distance[edg.a-1] + edg.w) else (distance[edg.b-1],0)
    if(not (flag)):
        break

print(distance)