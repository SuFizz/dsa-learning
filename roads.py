# -*- coding: utf-8 -*-
"""
Created on Wed May 31 19:38:19 2017

@author: sufiyans
"""

class city:
    def __init__(self,idx):
        self.idx = idx
        self.connect1 = {} #holds city to and road type
        self.connect2 = {} #holds city to and road type
        self.connect3 = {} #holds city to and road type
        self.m_visit = 0
    def connecter(self, to, typ):
        if(typ == 3):
            self.connect3[to] = 1
        elif (typ == 2):
            self.connect2[to] = 1
        else:
            self.connect1[to] = 1

def find_roads(cities):
    root = 0
    cities[root].m_visit = 1
    visitors = []
    visitors.append(root)
    for q in visitors:
        for j in cities[q].connect3:
            if(not cities[j-1].m_visit):
                cities[j-1].m_visit = 1
                visitors.append(j-1)
                print (q+1,j)
    
    for y in range(len(cities)):
        if not cities[y].m_visit:
            to = next(iter(cities[y].connect2.keys()))
            print (y+1, to)
            del cities[to-1].connect2[y+1]
    for y in range(len(cities)):
        if not cities[y].m_visit:
            to = next(iter(cities[y].connect1.keys()))
            print (y+1, to)
            del cities[to-1].connect1[y+1]

"""    
    visitors = []
    visitors.append(root)
    cities[root].m_visit = 1
    for q in visitors:
        for j in cities[q].connect2:
            if(not cities[j-1].m_visit):
                cities[j-1].m_visit = 1
                visitors.append(j-1)
                print (q+1,j)

    visitors = []
    visitors.append(root)
    for q in visitors:
        for j in cities[q].connect1:
            if(not cities[j].f_visit):
                cities[j].f_visit = 1
                visitors.append(j)
                print (q+1,j)
"""
line1 = input()
line1 = line1.split()
C = int(line1[0])
R = int(line1[1])

cities = [city(i) for i in range(C)]

for j in range(R):
    line = input()
    line = line.split()
    fr = int(line[0])
    to = int(line[1])
    ty = int(line[2])
    cities[fr-1].connecter(to,ty)
    cities[to-1].connecter(fr,ty)

find_roads(cities)