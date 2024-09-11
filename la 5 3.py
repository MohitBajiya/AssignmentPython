# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 12:52:03 2024

@author: DELL
"""
x1=0
x2=0
#Request the user to enter the value of 'd':-
d=int(input('Enter divisior'))

while 1:
    n=int(input("Enter the  integer:-"))
    if n==-999:
        break
    
    if n%d==0:
        x1+=1
    else:
        x2+=1
        
print(x1)
print(x2)
    