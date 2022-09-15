print("Enter a number to recieve its factors")
num1 = int(input())
count1 = num1
ans_list = []
for count in range (1, count1):
    num2 = num1 % count
    if num2 == 0:
        ans = num1 // count
        print(ans)

print("1")