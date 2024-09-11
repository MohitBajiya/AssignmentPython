# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 13:09:29 2024

@author: DELL
"""
#Request the user to enter the integer:-
a=int(input("Enter the integer:-"))
x=a
y=a
i=1
z=0
while a//10>0:
    i=i+1
    a=a//10
    
print(i)
    

while x>0:
    z=z+x%10*(10**(i-1))
    i=i-1
    x=x//10
print(z)
    

if z==y:
    print('it is pallindrome')