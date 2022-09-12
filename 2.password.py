# prompt the user to input a password
print("Please enter your password")
password = input()

# if statement to check if the password is more than 6 characters long
if len(password) > 6:
    print("Invalid password")
# end if

# if statement to check if the password is less than 7 characters long
if len(password) < 7:
    print("Valid password")
# end if