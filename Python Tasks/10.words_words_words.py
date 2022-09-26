print("Please enter a sentence")
sen = input()

count2 = 0

for count1 in range (1, len(sen) + 1):

    let = sen[count1 - 1]

    if let == " ":
        count2 = count2 + 1
    # end if

count2 = count2 + 1
print("The number of words in this sentence is", count2)