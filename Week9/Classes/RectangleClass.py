class Rectangle:

    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def __area(self):
        return self.__length*self.__width

    def __perimeter(self):
        return 2*(self.__length+self.__width)

    def __str__(self):
        return 'Length = '+str(self.__length)+'\n'\
               'Width = '+str(self.__width)+'\n'\
               'Area = '+str(self.__area())+'\n'\
               'Perimeter = '+str(self.__perimeter())

    #getters
    def get_length(self):
        return self.__length

    def get_width(self):
        return self.__width

    def get_area(self):
        return self.__area()

    def get_perimeter(self):
        return self.__perimeter()


r1 = Rectangle(20,22)
print(r1)

#print(r1.get_length())
#print(r1.get_width())
#print(r1.get_area())


