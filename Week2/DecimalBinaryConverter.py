import sys

def decimalToBinary():

    number = int(input("\nEnter a decimal number: "))

    i = 1
    result = 0

    while number > 0:
        remainder = int(number % 2)             #modulus of number
        result = result+(i*remainder)
        number = int(number/2)
        i = i*10

    print("\nBinary: ",result)

    print("\n******************************************************")

    Welcome()


def binaryToDecimal():

    number = input("\nEnter a binary number: ")

    numberLength = len(number)

    i = 1

    result = 0

    for i in range(1,numberLength+1):
        result = result+int(number[i-1])*2**(numberLength-i)

    print("\nDecimal: ",result)

    print("\n******************************************************")

    Welcome()


def Welcome():

    print("1. Decimal to Binary")

    print("\n2. Binary to Decimal")

    print("\n3. End")

    option = input("\nEnter option: ")

    print("\n******************************************************")

    if option == "1":
        decimalToBinary()

    elif option == "2":
        binaryToDecimal()

    elif option == "3":
        sys.exit()


Welcome()
