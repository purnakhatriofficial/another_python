class customer_name:
    def __init__(self, name, email, phone, password, balance):
        self.name = name
        self.email = email
        self.phone = phone
        self.password = password
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Invalid deposit amount. Please enter a positive value.")
            return
        self.balance += amount
        print(f"Deposited {amount}  New balance is {self.balance}.")

    def withdraw(self, amount):
          if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrew {amount}. Remaining balance is {self.balance}.")
          else:
              print("Insufficient balance, please refill your account.")

    def check_balance(self):
        print(f"{self.name}'s balance is {self.balance}.")

# Create customer instances with numeric balances
customer_one = customer_name("Purna Bahadur Khatri", "purnakhatri630@gmail.com", "9829839069", "Purna@#123", 60000)
customer_two = customer_name("Dammar Bahadur Khatri", "dammarkhatri630@gmail.com", "9829839789", "Dammar@#123", 20000)

# Perform transactions
customer_one.deposit(2000)
customer_one.withdraw(2000)

customer_two.deposit(20000)
customer_two.withdraw(12000)

# Check balances
customer_one.check_balance()
customer_two.check_balance()
