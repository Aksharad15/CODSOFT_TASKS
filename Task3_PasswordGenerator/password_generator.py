import random
import string

print("===================================")
print("      PASSWORD GENERATOR")
print("===================================")

while True:

    length = int(input("\nEnter desired password length: "))

    characters = ""

    uppercase = input("Include uppercase letters? (yes/no): ")
    if uppercase.lower() == 'yes':
        characters += string.ascii_uppercase

    lowercase = input("Include lowercase letters? (yes/no): ")
    if lowercase.lower() == 'yes':
        characters += string.ascii_lowercase

    numbers = input("Include numbers? (yes/no): ")
    if numbers.lower() == 'yes':
        characters += string.digits

    symbols = input("Include special characters? (yes/no): ")
    if symbols.lower() == 'yes':
        characters += string.punctuation

    if characters == "":
        print("\nError: You must select at least one character type!")
        continue

    password = ""

    for i in range(length):
        password += random.choice(characters)

    print("\nGenerated Password:")
    print(password)

    print("\n----------------------------")
    choice = input("Generate another password? (yes/no): ")

    if choice.lower() != 'yes':
        print("\nThank you for using Password Generator!")
        break