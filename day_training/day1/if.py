user = "ZCL"
passwd = "1234"

username = input("username:")
password = input("password:")

if username == user:
    print("Your username is correct...")
    if password == passwd:
        print("Logging successful...")
    else:
        print("Password error...")
else:
    print("Username error...")