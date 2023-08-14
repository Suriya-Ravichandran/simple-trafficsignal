#trafic signal program

#it is rules
print("press 1 is red,2 is yellow,3 is green, 4 is on the signal,5 is off the signal")

#get input to user
btn=int(input("Enter your option:"))

# work flow of this project
if(btn==1):
    print("Red")
elif(btn==2):
    print("Yellow")
elif(btn==3):
    print("Green")
elif(btn==4):
    print("signal is on")
else:
    print("signal is off please turn on signal")

