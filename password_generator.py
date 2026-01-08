import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def check_strength(password):
    if len(password) < 6:
        return "Weak"
    elif len(password) <= 10:
        return "Medium"
    else:
        return "Strong"

print("---- Password Generator & Strength Checker ----")

length = int(input("Enter password length: "))
password = generate_password(length)

print("Generated Password:", password)
print("Password Strength:", check_strength(password))
