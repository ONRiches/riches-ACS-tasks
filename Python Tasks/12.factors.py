# prompt the user to enter a number
print("Enter a number to recieve its factors")
num1 = int(input())
count1 = num1

for count in range (1, count1 + 1):

    # check if the count is a factor of the number
    num2 = num1 % count

    if num2 == 0:
        ans = num1 // count
        print(ans)
    # end if

# end for