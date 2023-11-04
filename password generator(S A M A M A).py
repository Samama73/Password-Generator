import random
import string

def generate_password(length, use_uppercase, use_lowercase, use_digits, use_special):
    characters = ''
    
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation
    
    if not characters:
        return "Complexity is too low. Please select at least one character type."
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

print("Password Complexity Options:")
print("1. Uppercase Letters")
print("2. Lowercase Letters")
print("3. Digits")
print("4. Special Characters")
complexity_options = input("Enter the numbers of the complexity options you want to include (e.g., 1234): ")

use_uppercase = '1' in complexity_options
use_lowercase = '2' in complexity_options
use_digits = '3' in complexity_options
use_special = '4' in complexity_options

length = int(input("Enter the desired password length: "))

password = generate_password(length, use_uppercase, use_lowercase, use_digits, use_special)

print("Generated Password:", password)
