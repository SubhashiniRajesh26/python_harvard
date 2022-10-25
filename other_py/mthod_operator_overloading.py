#operator (+) overloading
class Student:
	def __init__(self, m1, m2):
		self.m1 = m1
		self.m2 = m2

	def __add__(self, other):
		m1 = self.m1 + other.m1
		m2 = self.m2 + other.m2
		s3 = Student(m1, m2)
		return "{} {}".format(s3.m1, s3.m2)

s1 = Student(55, 56)
s2 = Student(62, 67)

s3 = s1 + s2

print(s3)

#method overloading
class Addition:
    def my_sum(self, a = None, b = None, c = None):
        s = 0
        if a != None and b != None and c != None:
            s = a + b + c
        elif a != None and b != None:
            s =  a + b
        return s


#method overriding
class A:
    def show(self):
        print("this is parent")

class B(A):
    def show(self):
        print("am child") #overrided

ob = B()
ob.show()
ob1 = A()
ob1.show()


obj = Addition()
print(obj.my_sum(10, 2))
print(obj.my_sum(10,11,22))
