# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 12:48:01 2024

@author: DELL
"""
#Request thwe user to enter the value of x:-
x=int(input("Enter the  integer:-"))
i=0
while x>0:
    i=i+x%10
    x=x//10
    
print(i)