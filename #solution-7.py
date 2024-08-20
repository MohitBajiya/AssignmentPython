#solution-7

# request the user to enter the Colour:-
colour=input("enter the colour Blue or Red")
# request the user to enter the mode:-
mode=input("enter the mode Steady or Flashing")
#If colour is blue and mode is steady then Request the user to print "clear view":-
if colour=="Blue" and mode=="Steady":
    print("clear view")

# If colour is Blue and mode is Flashing then Request the user to print "clouds due"
elif colour=="Blue" and mode=="Flashing":
    print("clouds due")

# If colour is Red and mode is Steady then Request the user to print "rain ahead:-"
elif colour=="Red" and mode=="Steady":
    print("rain ahead")

# If colour is Red and mode is Flashing then Request the user to print "snow instead:-"
elif colour=="Red" and mode=="Flashing":
    print("snow instead")
