from datetime import datetime
#staic or class variable
current_year = datetime.today().year

class Car:
    base_price = 100000
    def __init__(self, windows, doors, power):
        self.windows = windows
        self.doors = doors
        self.power = power
    def what_base_price(self):
        print("base price: {}".format(self.base_price))
    
    @classmethod
    def revised_base_price(cls, inflation):
        cls.base_price = cls.base_price + cls.base_price * inflation
    
    @staticmethod
    def check_year():
        if current_year <= 2022:
            return True
        else:
            return False

car1 = Car(4, 5, 3000)

if(Car.check_year()):
    pass
else:
    Car.revised_base_price(.10)

print(car1.base_price)