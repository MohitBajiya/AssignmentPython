#solution-3

# request the user to enter the weight:-
weight=int(input("enter your weight"))

# request the user to enter the height:-
height=int(input("enter your height"))

# BMI=Body Mass Index:-
BMI=(weight/(height)**2)

if BMI<18.5:
    print("you are underweight")
elif BMI>18.5 and BMI<25:
    print("you are normal weight")
elif BMI>25 and BMI<30:
    print("you are slightly overwweight")
elif BMI>30 and BMI<35:
    print("you are obese")
elif BMI>35:
    print("you are clinically obese")