print("Please enter a time in the format hours:minutes:seconds")
time = input()
count1 = 0

for count in range(1, len(time) + 1):
    
    let = time[count - 1]

    if count1 == 0:
        if let == ":":
            time1 = time[0:count-1]
            count1 = 1
            colon1 = count
        # end if
    # end if

    if count1 == 1:
        if let == ":":
            time2 = time[colon1:count-1]
            count1 = 1
            time3 = time[count+1:len(time)]
        # end if
    # end if

time1 = int(time1)
time2 = int(time2)
time3 = int(time3)

time1 = time1 * 60 * 60
time2 = time2 * 60
ans = time1 + time2 + time3

print(ans, "seconds")