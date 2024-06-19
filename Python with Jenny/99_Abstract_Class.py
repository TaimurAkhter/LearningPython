# Date: 27th January 2024 Saturday
# Start Time: 04 : 33 PM

# Date: 28th January 2024 Sunday
# Start Time: 04 : 11 PM
# End Time: 04 : 51 PM

from abc import ABC,abstractmethod


class Vehicle(ABC):
    def __init__(self, n):
        self.no_of_tyres = n
    @abstractmethod
    def start(self):
        pass

class Bike(Vehicle):
    def __init__(self, n, color):
        super().__init__(n)
        self.color = color
    def start(self):
        print("start with kick")
        
class Scooty(Vehicle):
    def __init__(self, n):
        super().__init__(n)
    def start(self):
        print("self start")

class Car(Vehicle):
    def __init__(self, n):
        super().__init__(n)
    def start(self):
        print("start with key")


bike = Bike(2, "Red")
bike.start()

car = Car(4)
car.start()

