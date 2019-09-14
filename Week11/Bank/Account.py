class Account():
    def __init__(self, accountName, accountNumber, branch, balance):
        self.__accountName = accountName
        self.__accountNumber = accountNumber
        self.__branch = branch
        self.__balance = balance

    #getters
    def get_accountName(self):
        return self.__accountName

    def get_accountNumber(self):
        return self.__accountNumber

    def get_branch(self):
        return self.__branch

    def get_balance(self):
        return self.__balance

    #setters
    def set_accountName(self, accountName):
        self.__accountName = accountName

    def set_accountNumber(self, accountNumber):
        self.__accountNumber = accountNumber

    def set_branch(self, branch):
        self.__branch = branch

    def set_balance(self, balance):
        self.__balance = balance

    def __str__(self):
        return 'Account name: ' + self.__accountName + '\n'\
                'Account number: ' + str(self.__accountNumber) +'\n'\
                'Branch: ' + self.__branch + '\n' + \
                'Balance: '+ str(self.__balance) + '\n'


b1 = Account("Matthew", 12345, "AIB", 1234.00)
print(b1)


