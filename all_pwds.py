# -*- coding: utf-8 -*-
"""
Created on Wed May 31 17:10:49 2017

@author: sufiyans
"""
global_outs = {}
def make_it(l,explored):
    for i in range(explored,len(l)):
        if l[i]=='s' or l[i] =='S':
            make_it(l,i+1)
            l[i] = '$'
            make_it(l,i+1)
            l[i] = 's'
        elif l[i]=='a' or l[i] =='A':
            make_it(l,i+1)
            l[i] = '@'
            make_it(l,i+1)
            l[i]='a'
    l = ''.join(l)
    global_outs[l] = 1

l ='Password passworder all the same heresies all this'
l = list(l)
explored = 0
make_it(l,explored)