import random

# get an input
print("Please enter R, P or S")
choice = input()

value = random.randint(1, 3)

# convert the input to a number     
RPS = ord(choice) % 10

# convert the 0 of a P to a 1
if RPS == 0:
    RPS = RPS + 1
# end if

# print our choice
if value == 1:
    print("P")
elif value == 2:
    print("R")
else:
    print("S")
# end if

# check win conditions for both sides
if RPS == 3 and value == 1:
    print("You win")
elif RPS == 1 and value == 3:
    print("I win")
elif RPS < value:
    print("You win")
elif RPS == value:
    print("Draw")
else:
    print("I win")
# end if