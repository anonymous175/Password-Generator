import string
import random

# Define the characters to include in the password
uppercase_letters = string.ascii_uppercase
lowercase_letters = string.ascii_lowercase
digits = string.digits
special_characters = string.punctuation

# Combine all characters
all_characters = uppercase_letters + lowercase_letters + digits + special_characters

# Set the length of the password
password_length = int(input("Enter Lenght: "))  # You can change the length of the password here

# Generate the password by randomly selecting characters from all_categories
password = ''.join(random.choice(all_characters) for _ in range(password_length))

print("Generated Strong Password:", password)
