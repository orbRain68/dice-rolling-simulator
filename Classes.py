class cars:
    def __init__(self,name,colour,price):
        self.name = name
        self.colour = colour
        self.price = price
    def carName(self):
        return (self.name)
    def carColour(self):
        return self.colour
    def carPrice(self):
        return self.price

car_1 = cars('BMW','Black','30000')
car_2 = cars('Nissan','Blue','15000')

#print(car_1.carName())
#print(car_2)
#print('This car is a really cool car it\'s call',car_1.name,'. But it\'s',car_1.price,'Dollers ,too much.')
#print(car_2.name)
print(f"The name is {car_1.carName()}, the colour of a car {car_1.carColour()}, and it cast around: {car_1.carPrice()}")
