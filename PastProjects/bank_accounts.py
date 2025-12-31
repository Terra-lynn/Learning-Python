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
    if amount > self.balance:
      print('Insufficient funds.')
    else:
      self.balance = self.balance - amount
      return amount

  def display_balance(self):
    print(self.balance)

USAA_Chera = BankAccount('Chera', 'Baumgartner', 12302025, 'Checking', 1234, 100)

USAA_Chera.deposit(96)
USAA_Chera.withdraw(25)
USAA_Chera.display_balance()
