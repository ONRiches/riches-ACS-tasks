# Prompt the user to enter a number
print("Enter a number between 1 - 3")
# Read the input
selection = int(input())

# Initialise a generic count variable
count = 0

# Use a while statement to keep prompting the user to enter an input until it is in the correct range
while count == 0:

    # check if the number is below 1
    if selection < 1:
        print("Enter a number between 1 - 3")
        selection = int(input())
    # end if

    # check if the number is above 3
    if selection > 3:
        print("Enter a number between 1 - 3")
        selection = int(input())
    # end if

    # if the number is in the correct range, stop the program and confrim the selection
    if selection < 4:

        if selection > 0:
            print("You have selected option", selection)
            count = count + 1
        # end if

    # end if

#end while