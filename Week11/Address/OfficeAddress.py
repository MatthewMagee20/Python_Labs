from Week11.Address.Address import Address as Parent

class OfficeAddress(Parent):
    def __init__(self, streetNumber, streetName, city, companyName, officeNumber):
         Parent.__init__(self, streetNumber, streetName,city)
         self.__companyName = companyName
         self.__officeNumber = officeNumber

    def get_companyName(self):
        return self.__companyName

    def get_officeNumber(self):
        return self.__officeNumber

    def set_companyName(self, companyName):
        self.__companyName = companyName

    def set_officeNumber(self, officeNumber):
        self.__officeNumber = officeNumber

    def __str__(self):
        return '\n' + super().__str__() + '\n' + \
               self.__companyName + '\n' + \
               str(self.__officeNumber)

oa1 = OfficeAddress(5, "Red Street", "Dublin", "Intel", 5)
print(oa1)
