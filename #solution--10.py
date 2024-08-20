#solution--10
# Request the user to enter the year:-
y=int(input("enter the year:-"))

if y%400==0 and y%4==0:
    print("leap year")
else:
    print("not a leap year")


