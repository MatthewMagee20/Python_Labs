class Address():
    def __init__(self, streetNumber, streetName, city):
        self.__streetNumber = streetNumber
        self.__streetName = streetName
        self.__city = city

    def get_streetNumber(self):
        return self.__streetNumber

    def get_streetName(self):
        return self.__streetName

    def get_city(self):
        return self.__city

    def set_streetNumber(self, streetNumber):
        self.__streetNumber = streetNumber

    def set_streetName(self, streetName):
        self.__streetName = streetName

    def set_city (self, city):
        self.__city = city

    def __str__(self):
        return  str(self.__streetNumber) + ' ' + self.__streetName + '\n'+\
                self.__city

a1 = Address(5, "Lakeview", "Cavan")
print(a1)
