# prompt the user to enter a number
print("Please enter a number in the range 100 - 999")
# read the input and convert the string to an integer
num1 = int(input())

# find the hundreds by integer divsion
hundreds = num1 // 100

# use a new variable to work out the tens and units
num2 = num1 % 100

# split the tens and units from each other
units = num2 % 10
tens = num2 // 10

# print the answer
print(hundreds, "hundreds", tens, "tens", units, "units")