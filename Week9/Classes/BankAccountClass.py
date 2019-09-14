class BankAccount:
    def __init__(self, accountName, accountNumber, branch, balance):
        self.__accountName = accountName
        self.__accountNumber = accountNumber
        self.__branch = branch
        self.__balance = balance

    def get_accountName(self):
        return self.__accountName

    def get_accountNumber(self):
        return self.__accountNumber

    def get_branch(self):
        return self.__branch

    def get_balance(self):
        return self.__balance

    def __str__(self):
        return 'Account name: '+self.__accountName+'\n'\
                'Account number: '+str(self.__accountNumber)+'\n'\
                'Branch: '+self.__branch+'\n'\
                'Balance: '+str(self.__balance)

B1 = BankAccount('Matthew Magee',12345,'Bank of Ireland',9999.00)
print(B1)
