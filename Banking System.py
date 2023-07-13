class BankAccount:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.initial_balance = 0

    def login(self, username, password):
        if username in credentials and credentials[username] == password:
            print("\t\t\t\t\tLogin successful!\n")
            print("\t*********Welcome to Infra Banking, Mr.", username.upper(), "*********")
            return True
        else:
            print("Invalid username or password.")
            return False

    def deposit(self, amount):
        if amount > 0:
            self.initial_balance += amount
            print("Deposited", amount, "Rupees. Current balance:", self.initial_balance, "Rupees.")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.initial_balance:
            self.initial_balance -= amount
            print("Withdrew", amount, "Rupees. Current balance:", self.initial_balance, "Rupees.")
        else:
            print("Invalid withdrawal amount or insufficient balance.")

    def get_balance(self):
        print("Your current balance is", self.initial_balance, "Rupees.")
    

# Create a dictionary to store username-password pairs
credentials = {
    "balu": "balu123",
    "abin": "abin123",
    "ayaan": "ayaan123"
}

print("\t***-----------Welcome to Infra banking-----------***\n")

print("Please enter your details for Login")

username1 = input("Enter your username: ")
password1 = input("Enter your password: ")


account = BankAccount(username1, password1)
if account.login(username1, password1):
    while True:
        print("\nBanking Operations:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Current Balance")
        print("4. Logout")


        choice = int(input("Enter your choice (1-4): "))
        if choice == 1:
            amount = int(input("Enter the deposit amount: "))
            account.deposit(amount)
        elif choice == 2:
            amount = int(input("Enter the withdrawal amount: "))
            account.withdraw(amount)
        elif choice == 3:
            account.get_balance()
        elif choice == 4:
            print("\t\t\t\t\tLogged out successfully\n"
                      "\n\t\t\t Thank you for using Infra Banking Service")
            break
        else:
                print("Invalid choice. Please try again.")

else:
    print("Login failed. Try again")
