# prompt the user to enter the three numbers to be sorted into decreasing order
print("Please enter the first of three numbers")
num1 = int(input())
print("Please enter the second of three numbers")
num2 = int(input())
print("Please enter the third of three numbers")
num3 = int(input())

if num1 > num2 and num1 > num3:
    
    if num2 > num3:
        print(num1, num2, num3)
    else:
        print(num1, num3, num2)
    # end if

elif num2 > num1 and num2 > num3:

    if num1 > num3:
        print(num2, num1, num3)
    else:
        print(num2, num3, num1)
    # end if

else:

    if num1 > num2:
        print(num3, num1, num2)
    else:
        print(num3, num2, num1)
    # end if

# end if