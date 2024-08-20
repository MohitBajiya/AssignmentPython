#solution--4

#request the user to enter the first number:-
x=int(input("enter the first number:"))
# request the user to enter the second number:-
y=int(input("enter the second number:"))

# if x>=0,Y>=0 and y%x==0 then request the user to print("y is divisible by x:-")
if x>=0: 
    if y>=0:
        if y%x==0:
            print("y is divisible by x")
        else:
            print("y is not divisible by x")

    else:
        print("input invalid")
else:
    print("input invalid") 

     
