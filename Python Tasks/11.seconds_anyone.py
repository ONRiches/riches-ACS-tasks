# prompt the user to enter the time
print("Please enter a time in the format hours:minutes:seconds")
time = input()
count1 = 0

for count in range(1, len(time) + 1):
    
    let = time[count - 1]

# find the first colon
    if count1 == 0:
        if let == ":":
            time1 = time[0:count-1]
            count1 = 1
            colon1 = count
        # end if
    # end if

# find the second colon
    if count1 == 1:
        if let == ":":
            time2 = time[colon1:count-1]
            count1 = 1
            time3 = time[count+1:len(time)]
        # end if
    # end if

# convert all strings to integers so that the seconds can be calculated
time1 = int(time1)
time2 = int(time2)
time3 = int(time3)

# calculate the seconds
time1 = time1 * 60 * 60
time2 = time2 * 60
ans = time1 + time2 + time3

# print the answer
print(ans, "seconds")