class Account:

    def __init__(self, filepath):
        self.filepath=filepath      #filepath and self.filepath not the same. we are using it to make filepath an instance variable we can use later
        with open(filepath,'r') as file:
            self.balance=int(file.read())   #self is object and balance is instance

    def withdraw(self, amount):
        self.balance=self.balance - amount

    def deposit(self, amount):
        self.balance=self.balance + amount

    def commit(self):
        with open(self.filepath, 'w') as file:
            file.write(str(self.balance))

account=Account("balance.txt")
print(account.balance)
account.deposit(100)
print(account.balance)
account.commit()
