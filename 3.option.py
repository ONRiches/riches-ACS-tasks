
print("Enter a number between 1 - 3")
selection = int(input())
count = 0
while count == 0:
    if selection < 1:
        print("Enter a number between 1 - 3")
        selection = int(input())
    if selection > 3:
        print("Enter a number between 1 - 3")
        selection = int(input())
    if selection < 4:
        if selection > 0:
            print("You have selected option", selection)
            count = count + 1