# Date: 19th January 2024 Friday
# Start Time: 02 : 33 PM
# End Time: 04 : 07 PM
# video 02m : 01s pr urdu boli

class Human: # Human class is known as Base/Parent/Supper Class
    def __init__(self, learn):
        self.learn = learn
        
    def date(self):
        print("Today is 19th January 2023")
        print("Time is 04 : 04 PM")
        
class Male(Human): # Male class is known as Derived/Child/Sub Class
    def __init__(self, name, learning):
        super().__init__(learning)
        self.name = name

    def display(self):
        print(f"I am learning {self.learn}")

    def todays_talk(self):
        super().date()
        print("Mein ny ab socha ky pta ni 1 ya 2 saal baad mein ty hn jayray classfellow mery naal prdy wa ona ny milna wi a ky nai.")
        

male_1 = Male("Taimur", "Python")
print(male_1.name)
male_1.display()
male_1.todays_talk()

 