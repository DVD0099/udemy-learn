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


class Checking(Account):

    def __init__(self,filepath,fee):
        Account.__init__(self,filepath)
        self.fee=fee                    #instance variable

    def transfer(self, amount):
        self.balance=self.balance - amount - self.fee

checking=Checking("balance.txt",1)
checking.transfer(100)
print(checking.balance)
checking.commit()
