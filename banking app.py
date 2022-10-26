
class bank:
    def __init__(self, initial_amount=0):
        self.balance = initial_amount

        
    def deposit(self, name, amount):
        self.name = name
        self.amount = amount
        self.balance = self.balance + amount
        message = f'Transaction successful {name} ksh {amount} has been deposited to your account.\n your new balance is {self.balance}.\n'
        with open('transaction_receipt.txt', 'a') as f:
            f.write(message)
        print(name, amount)
        

    def withdraw(self, name, amount):
        self.name = name
        self.balance = self.balance - amount
        message = f'Transaction successful {name} you have withdrawn ksh {amount} from your account.\n Your new balance is {self.balance}.\n'
        with open('transaction_receipt.txt', 'a') as f:
            f.write(message)


account = bank(1000000)
while True:
    transaction = input('Do you want to withdraw or deposit?')
    transaction = transaction.lower()
    if transaction in ['withdraw', 'deposit']:
        if transaction == 'withdraw':
            amount = input('How much do you want to withdraw? ')
            amount = float(amount)
            name = input('what is your username? ')
            name = name.lower()
            account.withdraw(name, amount)
            
        elif transaction == 'deposit':
            amount = input('How much do you want to deposit? ')
            amount = float(amount)
            name = input('what is your username? ')
            name = name.lower()
            account.withdraw(name, amount)
            
