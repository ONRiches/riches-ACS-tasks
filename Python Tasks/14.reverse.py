# prompt the user to enter a string
print("Pleae enter a word to be reversed")
# read the input and convert it to a list
text2 = input()
text = list(text2)

# reverse the list
text.reverse()

# convert the list back to a string
text1 = ''.join(text)

# print the string
print(text1)

if text1 == text2:
    print("This word is a pallindrome")
# end if