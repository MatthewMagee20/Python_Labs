class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def totalPrice(self):
        return self.price*self.quantity

    def __str__(self):
        return  'Item name: '+ self.name + '\n'\
                'Item price: ' + str(self.price) + '\n'\
                'Quantity : ' + str(self.quantity) + '\n'\
                'Total price: ' + str(self.totalPrice()) +'\n'


iphone = Item('IPhone',500.00,12)
samsung = Item('Samsung',750.00,24)

print(iphone)
print(samsung)


