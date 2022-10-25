class Car:
    base_price = 100000
    def __init__(self, windows, doors, power):
        self.__windows = windows
        self.doors = doors
        self.power = power
c1 = Car(3, 4, 1000)
# print(c1.__windows)
print(c1._Car__windows)
class Truck(Car):
    def __init__(self, windows, doors, power, engine_type):
        super().__init__(windows, doors, power)
        self.engine_type = engine_type
    
class Lorry(Truck):
    def __init__(self, windows, doors, power, engine_type, capacity):
        super().__init__(windows, doors, power, engine_type)
        self.capacity = capacity


# car1 = Car(4, 4, 2000)
# car1.__windows = 3
# print(car1.__windows)
truck1 = Truck(4, 3, 4000, 'Diesel')
truck1.__windows = 1
print(truck1.__windows)
# # print(dir(truck1))
# # print(dir(car1))
# truck1.__windows = 1
# print(truck1.__windows)
# lorry1 = Lorry(1, 2, 5000, 'diesel', 500)
# lorry1.__windows = 5
# print(lorry1.__windows)
