print("Please input your sentence to put turned into cyphertext")
text = list(input())

for count in range (1, len(text) + 1):
    char = ord(text[count - 1])

    if char == 121:
        char = 97
    elif char == 122:
        char = 98
    else:
        char = char + 2
    # end if

    text[count - 1] = chr(char)
# end for

newtext = ''.join(text)
print(newtext)