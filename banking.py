users = {"user1": {"password": "pass1", "balance": 1000}}

def login():
    username = input("Username: ")
    password = input("Password: ")
    if username in users and users[username]["password"] == password:
        print("Login successful!")
        dashboard(username)
    else:
        print("Invalid credentials!")

def dashboard(username):
    while True:
        print("\n1. Check Balance\n2. Deposit\n3. Withdraw\n4. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            print(f"Balance: {users[username]['balance']}")
        elif choice == "2":
            amt = float(input("Amount to deposit: "))
            users[username]['balance'] += amt
            print("Deposited successfully.")
        elif choice == "3":
            amt = float(input("Amount to withdraw: "))
            if amt <= users[username]['balance']:
                users[username]['balance'] -= amt
                print("Withdrawn successfully.")
            else:
                print("Insufficient balance.")
        elif choice == "4":
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    login()
