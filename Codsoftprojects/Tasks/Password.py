#Password Generator
import random
import string

print("🔑 ......Welcome to Password Generator.....🔑")

length= int(input("Enter The length of Password (minimum 6 characters): "))
print("Choose The Type Of Password You want To Generate-->")
print("1. Simple Password(only lowercase letters)")
print("2. Medium Password(lowercase and uppercase letters)")
print("3. Strong Password(lowercase, uppercase, digits and special characters)")
choice = int(input("Enter Your Choice (1,2,3): "))
if length < 6:
    print("Password length should be at least 6 characters.")
elif choice == 1:
    characters = string.ascii_lowercase
    password = ''.join(random.choice(characters) for i in range(length))
    print("Generated Simple Password: ", password)
elif choice == 2:
    characters = string.ascii_letters
    password = ''.join(random.choice(characters) for i in range(length))
    print("Generated Medium Password: ", password)
elif choice == 3:
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    print("Generated Strong Password: ", password)
else:
    print("Invalid Choice")

print("Thank You For Using Password Generator 🔐")