# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class edge():
    def __init__(self, a, b):
        self.a = a
        self.b = b

class vertex():
    def __init__(self,idx):
        self.index = idx
        self.adj = []
        self.in_degree = 0
        self.visited = 0
    def add_vertex(self,b):
        self.adj.append(b)
    def in_degree_inc(self):
        self.in_degree += 1

line1 = input()
N=int(line1.split()[0])
M=int(line1.split()[1])

edges = []
vertices = [vertex(i) for i in range(N)]

for j in range(M):
    line = input()
    line = line.split()
    a = int(line[0])
    b = int(line[1])
    edges.append(edge(a,b))
    vertices[a-1].add_vertex(b)
    vertices[b-1].in_degree_inc()

#implementing BFS to get the sort

Q = [v for v in vertices if v.in_degree == 0]

if Q == []:
    Q.append(min(vertices), key=lambda vertex:vertex.in_degree)

for q in Q:
    if(not(q.visited)):
        print(q.index+1)
        for v in q.adj:
            Q.append(vertices[v-1])
        q.visited = 1