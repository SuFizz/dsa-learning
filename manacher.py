# -*- coding: utf-8 -*-
"""
Created on Sun May 21 12:13:37 2017

@author: sufiyans
"""

string_to_check = input()
string_to_check = string_to_check.replace("","#")
string_to_check = "$"+string_to_check+"@"
es = list(string_to_check)

pos = [0]*len(es)
centre = 0
right_bnd = 0

for i in range(1,(len(es)-1)):
    mirror = 2*centre - i
    if(i<right_bnd):
        pos[i] = min(right_bnd-i, pos[mirror])
    while(es[i + (pos[i]+1) ] == es[i- (pos[i]+1)]):
        pos[i]+=1
    if(i+pos[i] > right_bnd):
        centre = i
        right_bnd = i + pos[i]
print (pos)