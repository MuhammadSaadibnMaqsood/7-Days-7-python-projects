class ATM:

    def __init__(self, balance):
        self.balance = balance

    def deposite(self, amount):
        self.balance += amount
        print(
            f"Your Amount deposite successfully! Your current balance is ${self.balance}"
        )

    def withdraw(self, amount):

        if amount > self.balance:
            print("Insufficent Balance")
            return
        self.balance -= amount
        print(f"With draw successfully! Your current balance is ${self.balance}")

    def check_balance(self):
        print("Your current Balance is $", self.balance)


atm = ATM(2000)
print("Welcome to the XYZ Bank")
print("-" * 20)
while True:

    choice = int(
        input(
            "Enter your choice between (1-3) \n1.Deposite\n2. With Draw\n3. Check Balance\n4. Exit\n"
        )
    )

    if choice == 1:
        amount = int(input("Enter Amount $"))
        atm.deposite(amount=amount)
    elif choice == 2:
        amount = int(input("Enter Amount $"))
        atm.withdraw(amount=amount)
    elif choice == 3:
        atm.check_balance()
    elif choice == 4:
        print("Thank for using ATM!")
        break
    else:
        print("Invalid choice please choose between (1-3)")
