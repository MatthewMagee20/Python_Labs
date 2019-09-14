class ComplexNumber:
    def __init__(self, realA, realB):
        self.realA = realA
        self.realB = realB

    def __add__(self, other):
        addA = self.realA + other.realA
        addB = self.realB + other.realB

        return "\nAdded Number: " + str(addA) + '+' + str(addB) + 'i'

    def __sub__(self, other):
        subA = self.realA - other.realA
        subB = self.realB - other.realB

        return "\nSubtracted: " + str(subA) + '+' + str(subB) + 'i'


    def __str__(self):
        return  'Original: ' + str(self.realA) + '+' + str(self.realB) + 'i'


c1 = ComplexNumber(1,2)
c2 = ComplexNumber(5,6)
added = c1 + c2
subtracted = c1 - c2

print(c1)
print(c2)
print(added)
print(subtracted)
