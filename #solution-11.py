#solution-11
# request the user to enter the first number:-
num1=input("enter the first number:")
# request the user to enter the second number:-
num2=input("enter the second number:")
# request the user to enter the third number:-
num3=input("enter the third number:")

if num1>=num2 and num1>=num3:
    print("num1")

elif num2>=num1 and num2>=num3:
    print("num2")
    
elif num3>=num1 and num3>=num2:
    print("num3")
