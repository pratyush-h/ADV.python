# register
with open("users.txt", "a") as f:
    user = input("Username: ")
    pwd = input("Password: ")
    f.write(user + "," + pwd + "\n")

# login
user = input("Enter username: ")
pwd = input("Enter password: ")

with open("users.txt", "r") as f:
    for line in f:
        u, p = line.strip().split(",")
        if u == user and p == pwd:
            print("Login successful")
            break
    else:
        print("Invalid credentials")