# Date: 30th January 2024 Tuesday
# Start Time : 04 : 00 PM
# End Time : 04 : 37 PM

from P102_B import Student

class A(Student):
    def __init__(self, name, city, age):
        super().__init__(name)
        self.city = city
        self.__age = age
    def show(self):
        print(f"Hey I am {self.name} from {self.city}")
    def private(self):
        print(f"My age is {self.__age}.")

class B(Student):
    def __init__(self, name, city, age):
        super().__init__(name)
        self.city = city
        self.__age = age
    def show(self):
        print(f"Hey I am {self.name} from {self.city}")
    def __private(self):
        print(f"My age is {self.__age}.")

