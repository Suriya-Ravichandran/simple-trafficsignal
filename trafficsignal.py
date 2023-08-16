# Traffic signal program with loop
print("Press 1 for red, 2 for yellow, 3 for green, 4 to turn on the signal, 5 to turn off the signal, or 0 to exit")
while True:
    # Display rules
    

    # Get input from user
    btn = int(input("Enter your option: "))

    # Workflow of this project
    if btn == 1:
        print("Red")
    elif btn == 2:
        print("Yellow")
    elif btn == 3:
        print("Green")
    elif btn == 4:
        print("Signal is on")
    elif btn == 5:
        print("Signal is off. Please turn on the signal.")
    elif btn == 0:
        print("Exiting the program.")
        break  # Exit the loop if the user chooses to exit
    else:
        print("Invalid option")

