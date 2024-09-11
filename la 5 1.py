# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 12:31:59 2024

@author: DELL
"""
#Lab5-Q1
#Request thwe user to enter the value of x and y:-
a= int(input("Enter the first integer:-"))
b=int(input("Enter the second integer:-"))
n=int(input("Enter divisior"))
#if i%n==0 then request the user to print(i)
for i in range(a,b+1):
    if i%n==0:
        print(i)