#solution--3
# Request the user to enter the length of plot:-
length=int(input("enter the length in feet:"))

# Request the user to enter the width of plot:-
width=int(input("enter the width in feet:"))

# there a is area of plot :-
a=length*width*0.093

if length*width>=0:
    print(a)
# a is "sq.m"
else:
    print("enter positive length and width")