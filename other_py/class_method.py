from datetime import date, datetime
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display(self):
        print("Name: " + self.name + "\n" + "Age : {}".format(self.age))

    @classmethod
    def current_age(cls, birth_year):
        # cls.name = name
        cls.age = date.today().year - birth_year
        return cls.age

p1 = Person("Subhashini", 28)
p1.display()

# Person.current_age("Subhashini", 1992)
# print(Person.age)

Person.current_age(1993)
print(Person.age)