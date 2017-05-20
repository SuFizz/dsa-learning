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
    def __init__(self,index,N):
        self.index = index
        self.weights = [math.inf]*N
        self.visited = 0
    def weight(self,b,w):
        self.weights[b-1] = w

def add_more_adjacent_edges(adjacent_edges,min_edge, min_edge_idx,vertices):
    del adjacent_edges[min_edge_idx]
    #print ("here2")
    #print("here2",adjacent_edges)
    if(vertices[min_edge.a -1].visited):
        vertices[min_edge.b -1].visited = 1
        for j in range(len(vertices[min_edge.b-1].weights)):
            if(vertices[min_edge.b-1].weights[j] < math.inf):
                adjacent_edges.append(edge(min_edge.b,j+1,vertices[min_edge.b-1].weights[j]))
        #return min_edge.b
    else:
        vertices[min_edge.a-1].visited = 1
        for j in range(len(vertices[min_edge.a-1].weights)):
            if(vertices[min_edge.a-1].weights[j] < math.inf):
                adjacent_edges.append(edge(min_edge.a,j+1,vertices[min_edge.a-1].weights[j]))
    #print ("here3",adjacent_edges)
        #return min_edge.a

def find_next_vertex(vertices, adjacent_edges):
    #print (adjacent_edges)
    sumi = 0
    while 1:
        #print ("here1",adjacent_edges)
        for q in range(len(adjacent_edges)):
            mini_edge = heapq.nsmallest((1+q), ((k.w,j,k) for j,k in enumerate(adjacent_edges)) )
            min_edge = mini_edge[q][2]
            min_edge_idx = mini_edge[q][1]
            #print(min_edge.w,min_edge.a,min_edge.b)
            if(not(vertices[min_edge.a -1].visited and vertices[min_edge.b-1].visited)):
                sumi += min_edge.w
                add_more_adjacent_edges(adjacent_edges, min_edge, min_edge_idx, vertices)
                break
        if not(sum([(1-i.visited) for i in vertices]) > 0):
            break
    return sumi

line1 = input()
N=int(line1.split()[0])
M=int(line1.split()[1])

vertices = []
for j in range(N):
    vertices.append(vertex(j,N))

for j in range(M):
    line = input()
    line = line.split()
    a = int(line[0])
    b = int(line[1])
    w = int(line[2])
    vertices[a-1].weight(b,w)
    vertices[b-1].weight(a,w)

vertices[0].visited = 1
adjacent_edges = []

for j in range(N):
    if(vertices[0].weights[j] < math.inf):
        adjacent_edges.append(edge(1,j+1,vertices[0].weights[j]))

sumi = find_next_vertex(vertices, adjacent_edges)

#for v in vertex:
#    
#    if(v):
#    
#
#for a in range(N):
#    visited[a] = 1
#    for q in range(N):
#        elem = heapq.nsmallest(q+1, ((k,j) for j,k in enumerate(vertex[a])))
#        b = elem[q][1]
#        w = elem[q][0]
#        print (a+1, b+1,w)
#        if(not(visited[b])):
#            visited[b] =1
#            sum += w
#            break
print (sumi)