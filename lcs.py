# -*- coding: utf-8 -*-
"""
Created on Wed May 31 14:48:25 2017

@author: sufiyans
"""

str1 = input()
str2 = input()
maxi = 0
long_str = []

table = [[0 for j in range(len(str2))] for i in range(len(str1))]

for i in range(len(str1)):
    for j in range(len(str2)):
        if(str2[j] == str1[i]):
            if(i>0 and j>0):
                table[i][j] = table[i-1][j-1]+1
            else:
                table[i][j] = 1
            if table[i][j] > maxi:
                maxi = table[i][j]
                long_str = []
                long_str.append(str1[(i-maxi+1) : i+1])
            elif table[i][j] == maxi:
                long_str.append(str1[(i-maxi+1) : i+1])
print(table,long_str,maxi)