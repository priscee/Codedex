class BankAccount:
  def __init__(self, first_name, last_name, account_id, account_type, pin, balance):
    self.first_name = first_name
    self.last_name = last_name
    self.account_id = account_id
    self.account_type = account_type
    self.pin = pin
    self.balance = balance

  def deposit(self, amount):
    self.balance = self.balance + amount
    return self.balance
  
  def withdraw(self, amount):
    self.balance = self.balance - amount
    return self.balance

  def display_balance(self):
    print(f"{self.balance}")

account = BankAccount("Jane", "Doe", 333666999, "Savings", "2468", 1000000.00)

account.deposit(96)
account.display_balance()

account.withdraw(25)
account.display_balance()