# Date: 30th January 2024 Tuesday
# Start Time : 04 : 00 PM
# End Time : 04 : 37 PM

from abc import ABC,abstractmethod

class Student(ABC):
    def __init__(self, name):
        self.name = name
    @abstractmethod
    def show(self):
        pass

