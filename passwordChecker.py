import string

# Prompt the user to enter a password
password = input("Enter your password: ")

# Check for the presence of various character types
uppercase = any([1 if c in string.ascii_uppercase else 0 for c in password])
lowercase = any([1 if c in string.ascii_lowercase else 0 for c in password])
Special_case = any([1 if c in string.punctuation else 0 for c in password])
digits = any([1 if c in string.digits else 0 for c in password])

characters = [uppercase, lowercase, Special_case, digits]
length = len(password)
score = 0

# Check if the password is common
with open('Password Strength checker\conmonPass.txt', 'r') as f:
    commonPass = f.read().splitlines()
if password in commonPass:
    print("Password is common")
    exit()

# Score based on password length
if length > 8:
    score += 1
if length > 12:
    score += 1
if length > 16:
    score += 1
if length > 20:
    score += 1

print(f"Password length is {str(length)}, adding {str(score)} points!")

# Score based on character variety
if sum(characters) > 1:
    score += 1
if sum(characters) > 2:
    score += 1
if sum(characters) > 3:
    score += 1

print(f"Password has {str(sum(characters))} different character types, adding {str(sum(characters) - 1)} points.")

# Evaluate password strength
if score < 4:
    print(f"The password is weak!")
elif score == 4:
    print('This password is ok.')
elif 4 <= score < 6:
    print("This password is good!")
elif score >= 6:
    print('This password is strong!')
