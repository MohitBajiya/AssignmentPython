# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 16:09:24 2024

@author: USER
"""

x=int(input("enter the divisor:"))
d1=0
d2=0
while 1:
    n=int(input("enter any number:-"))
    if n==-999:
        break
    else:
        if n%x==0:
            d1+=1
        else:
            d2+=1
        print(d1)
        print(d2)