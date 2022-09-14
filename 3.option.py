# Prompt the user to enter a number
print("Enter a number between 1 - 3")
# Read the input
selection = int(input())

notfound = False

# Use a while statement to keep prompting the user to enter an input until it is in the correct range
while not(notfound):

    # check if the number is below 1
    if selection < 1 or selection > 3:
        print("Enter a number between 1 - 3")
        selection = int(input())
    else:
        print("You have selected option", selection)
        notfound = True
    # end if

#end while