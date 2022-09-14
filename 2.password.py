# prompt the user to input a password
print("Please enter your password")
password = input()

# if statement to check if the password is more than 6 characters long
if len(password) > 6 or len(password) < 1:
    print("Invalid password")
else:
    print("Valid password")
# end if