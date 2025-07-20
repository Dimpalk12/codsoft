import random

print("\n Welcome to Dimpal's  Password Generator!")
name = input(" What's your name? ")



length_input = input(" How long should your password be? (Minimum 4): ")
if length_input.isdigit():
    password_length = int(length_input)
else:
    print(" Please type a number next time")
    exit()

if password_length < 4:
    print(" Password must be at least 4 characters long!")
    exit()

#  Characters we can use
letters = "abcdeghijklmnopqrstuvwxyz"
big_letters = "ABCDEFGHJKLMNPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%"

# Combine all characters
all_chars = letters + big_letters + numbers + symbols

#  Create password by picking random characters
password = ""

for i in range(password_length):
    char = random.choice(all_chars)
    password = password + char  

print("\n Your password is ready!")
print(" Password: " + password)
print("\n Don't share your password with anyone else")

print("\nThanks for using Dimpal's  Password Generator", name)