class BankAccount:
    def __init__(self, accountName, accountNumber, branch, balance, depositAmount, withdrawAmount):
        self.__accountName = accountName
        self.__accountNumber = accountNumber
        self.__branch = branch
        self.__balance = balance
        self.__depositAmount = depositAmount
        self.__withdrawAmount = withdrawAmount

    def __deposit(self, balance, depositAmount):
        balance = depositAmount + balance
        return balance

    def __withdraw(self, balance, withdrawAmount):
        balance = balance - withdrawAmount

        if balance < 0:
            print("Balance is negative")

        else:
            return balance

    def get_accountName(self):
        return self.__accountName

    def get_accountNumber(self):
        return self.__accountNumber

    def get_branch(self):
        return self.__branch

    def get_balance(self):
        return self.__balance

    def get_depositAmount(self):
        return self.__depositAmount

    def get_withdrawAmount(self):
        return self.__withdrawAmount

    def __str__(self):
        return 'Account name: '+self.__accountName+\
                'Account number: '+self.__accountNumber+\
                'Branch: '+self.__branch+\
                'Balance: '+self.__
