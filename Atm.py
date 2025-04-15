class ATM:
    def __init__(self, users):
        self.users = users
        self.current_user = None

    def login(self):
        print("===== Welcome to ATM Bank =====")
        card = input("Enter your card number: ")
        pin = input("Enter your PIN: ")

        if card in self.users and self.users[card]['pin'] == pin:
            self.current_user = card
            print(f"\nLogin successful. Welcome, {self.users[card]['name']}!\n")
        else:
            print("\nInvalid card number or PIN. Please try again.\n")
            return False
        return True

    def show_menu(self):
        while True:
            print("====== ATM Details ======")
            print("1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                self.check_balance()
            elif choice == '2':
                self.deposit()
            elif choice == '3':
                self.withdraw()
            elif choice == '4':
                print("\nThank you for using ATM Bank. Goodbye!\n")
                break
            else:
                print("Invalid choice. Try again.\n")

    def check_balance(self):
        balance = self.users[self.current_user]['balance']
        print(f"\nYour current balance is: ${balance:.2f}\n")

    def deposit(self):
        amount = float(input("Enter amount to deposit: "))
        if amount > 0:
            self.users[self.current_user]['balance'] += amount
            print(f"${amount:.2f} deposited successfully.\n")
        else:
            print("Invalid amount.\n")

    def withdraw(self):
        amount = float(input("Enter amount to withdraw: "))
        balance = self.users[self.current_user]['balance']
        if amount > 0 and amount <= balance:
            self.users[self.current_user]['balance'] -= amount
            print(f"${amount:.2f} withdrawn successfully.\n")
        elif amount > balance:
            print("Insufficient balance.\n")
        else:
            print("Invalid amount.\n")


users_data = {
    '123456': {'name': 'Sai', 'pin': '1111', 'balance': 1500.0},
    '654321': {'name': 'Vivek', 'pin': '2222', 'balance': 1000.0}
}

atm = ATM(users_data)

if atm.login():
    atm.show_menu()
