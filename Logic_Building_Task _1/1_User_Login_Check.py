username = "admin"
password = "1234"

input_usernm = input("Enter username: ")
input_pass = input("Enter password: ")

if input_usernm == username and input_pass== password:
    print("Login Successful")
else:
    print("Invalid Credentials")
