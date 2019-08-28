Password = input("Enter Password: ")
min_length = 5

if len(Password) < min_length:
    Password = input("Enter Password: ")

print(len(Password) * "*")