# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class edge():
    def __init__(self, a, b, w):
            self.a = a
            self.b = b
            self.w = w

line1 = input()
N=int(line1.split()[0])
M=int(line1.split()[1])

edges = []

for j in range(M):
    line = input()
    line = line.split()
    a = int(line[0])
    b = int(line[1])
    w = int(line[2])
    edges.append(edge(a,b,w))
    
sort_edges = sorted(edges, key=lambda edge:edge.w)

sets = []

sum = 0
for elem in sort_edges:
    flag = 0
    for j in sets:
        if((elem.a in j) or (elem.b in j)):
            if((elem.a in j) and (elem.b in j)):
                flag = 1
                break
            elif(elem.a in j):
                flag = 1
                sum += elem.w
                j.append(elem.b)
                break
            else:
                flag = 1
                sum += elem.w
                j.append(elem.a)
                break
        if(flag == 1):
            break
    if(flag == 0):
        sum+=elem.w
        sets.append([elem.a,elem.b])    
print (sum)