username = input("Enter Username: ")

if username == "Labib1234":
    password = int(input("Your Username is correct \nEnter Password: "))
    if (password == 12345):
        print("YOU SHALL PASS")
    else:
        print("Your password is wrong.\nYOU SHALL NOT PASS")
else:
    print("Your username is wrong. \nYOU SHALL NOT PASS")