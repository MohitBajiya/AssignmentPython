# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 13:19:39 2024

@author: DELL
"""
#Request the user to enter the integer:-
x=int(input("Enter the integer:-"))
l=1
k=1
s=0
print(1)
print(1)
while x>2:
    
    s=l+k
    k=l
    l=s
    
    x=x-1
#Request the user to print(s)
    print(s)