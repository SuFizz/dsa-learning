# -*- coding: utf-8 -*-
"""
Created on Wed May 31 16:35:53 2017

@author: sufiyans
"""
import heapq

class city:
    def __init__(self, idx, ppl):
        self.dev_idx = idx
        self.ppl = ppl

line1 = input()
line1 = line1.split()
N = int(line1[0])
K = int(line1[1])
cities = []
tot_votes = 0
for i in range(N):
    line = input()
    line = line.split()
    idx = int(line[0])
    ppl = int(line[1])
    if(idx):
        cities.append(city(idx,ppl))
    else:
        tot_votes += ppl

mini_edge = heapq.nsmallest((K), (j.ppl for j in cities))
maxi_edge = heapq.nlargest((K), (j.ppl for j in cities))

print ((sum(mini_edge)+tot_votes),(sum(maxi_edge)+tot_votes))