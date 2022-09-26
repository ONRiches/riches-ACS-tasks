# prompt the user to end the number to be divided
print("Please enter the number to be divided")
num1 = int(input())


# prompt the user to enter the divisor
print("Please enter the divisor")
div = int(input())

# find the answer to the integer division and the remainder
ans = num1 // div
rem = num1 % div

# print the answer and remainder
print(ans, "remainder", rem)