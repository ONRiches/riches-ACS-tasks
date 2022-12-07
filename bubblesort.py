import winsound
list = [1,6,32,7,9,3,1,5,8,3,5,8]
n = len(list)

for i in range (0,n-1):
    for j in range (0, n-i-1):
        if list[j] > list[j+1]:
            temp = list[j+1]
            list[j+1] = list[j]
            list[j] = temp
            winsound.Beep(1200,40)

print(list)