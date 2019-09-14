from Week11.Bank.CurrentAccount import CurrentAccount

class SavingsAccount(CurrentAccount):
        def __init__(self, accountName, accountNumber, branch, balance, depositAmount, withdrawAmount):
            CurrentAccount.__init__(self, accountName, accountNumber, branch, balance, depositAmount, withdrawAmount)
            self.__balance = balance

        def __interestCalc(self):
            self.__balance = self.__balance + (self.__balance * 0.05)
            return self.__balance

        def __str__(self):
            return super().__str__() + '\n'\
            'Amount after 1 year: ' + str(self.__interestCalc())


s1 = SavingsAccount("Mark", 10100005, "BOI", 1000.0, 200, 122)
print(s1)
