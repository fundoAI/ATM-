class ATM:
    def __init__(self):
        self.pin = "1969"
        self.balance = 1000
        self.attempts = 0

    def check_pin(self):
        while self.attempts < 3:
            user_pin = input("Enter your PIN: ")
            if user_pin == self.pin:
                return True
            else:
                self.attempts += 1
                print(f"Incorrect PIN. Attempts remaining: {3 - self.attempts}")
        return False

    def display_menu(self):
        print("\nATM Menu:")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

    def main(self):
        if self.check_pin():
            while True:
                self.display_menu()
                choice = input("Enter your choice: ")
                if choice == "1":
                    print(f"Your current balance is: {self.balance}")
                elif choice == "2":
                    amount = float(input("Enter amount to deposit: "))
                    self.balance += amount
                    print(f"Deposit successful. Your new balance is: {self.balance}")
                elif choice == "3":
                    amount = float(input("Enter amount to withdraw: "))
                    if amount > self.balance:
                        print("Insufficient funds.")
                    else:
                        self.balance -= amount
                        print(f"Withdrawal successful. Your new balance is: {self.balance}")
                elif choice == "4":
                    print("Exiting the program. Goodbye!")
                    break
                else:
                    print("Invalid choice. Please try again.")
        else:
            print("Maximum attempts exceeded. Card blocked.")

# Create an ATM object and start the program
atm = ATM()
atm.main()
