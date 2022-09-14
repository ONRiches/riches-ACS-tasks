# prompt the user to enter two number to be sorted into decreasing order
print("Please input the first of two numbers")
num1 = int(input())
print("Please input the second of two numbers")
num2 = int(input())

if num1 > num2:
    print(num1, num2)
else:
    print(num2, num1)
#end if