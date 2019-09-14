from Week11.Bank.Account import Account as Parent


class CurrentAccount(Parent):

    def __init__(self, accountName, accountNumber, branch, balance, depositAmount, withdrawAmount):
        Parent.__init__(self, accountName, accountNumber, branch, balance)
        self.__balance = balance
        self.__depositAmount = depositAmount
        self.__withdrawAmount = withdrawAmount

    def __deposit(self):
        self.__balance = self.__depositAmount + self.__balance
        return self.__balance

    def __withdraw(self):
        self.__balance = self.__balance - self.__withdrawAmount

        if self.__balance == 0:
            return "Balance is 0!"
        elif self.__balance < 0:
            return "Balance is " + str(self.__balance)
        else:
            return self.__balance

    def get_depositAmount(self):
        return self.__depositAmount

    def get_withdrawAmount(self):
        return self.__withdrawAmount

    def set_depositAmount(self, depositAmount):
        self.__depositAmount = depositAmount

    def set_withdrawAmount(self, withdrawAmount):
        self.__withdrawAmount = withdrawAmount

    def __str__(self):
        return super().__str__() + \
            'Deposit amount: ' + str(self.__depositAmount) + '\n'\
            'Withdraw amount: ' + str(self.__withdrawAmount) + '\n'\
            'After Deposit: ' + str(self.__deposit()) + '\n'\
            'After withdraw: ' + str(self.__withdraw()) + '\n'


ca1 = CurrentAccount("Person1", 1000001, "BOI", 20.0, 150, 10)
ca2 = CurrentAccount("Person2", 1000002, "BOI", 50, 0, 50)
ca3 = CurrentAccount("Person3", 1000003, "BOI", 200, 200, 500)

print(ca1)
print(ca2)
print(ca3)
