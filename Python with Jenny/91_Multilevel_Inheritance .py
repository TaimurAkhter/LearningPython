# Date: 19th January 2024 Friday
# Time: 05 : 09 PM

# Date: 20th January 2024 Saturday
# Start Time: 08 : 46 PM
# End Time : 10 : 56 : 45s PM

class Human:
    can_breath = True
    def __init__(self, num_heart):
        # print("Calling init from human class") 
        self.eyes = 2
        self.num_heart = num_heart

    def eat(self):
        print("I can eat")
    def work(self):
        print("I can work")

class Male(Human):
    def __init__(self, name):
        # print("Calling init from male class")
        self.name = name
        
    def sleep(self):
        print("I sleep upto 7 or 8 hours")
        
class Boy(Male):
    def __init__(self, heart, name, your_class):
        Human.__init__(self, heart)
        Male.__init__(self, name)
        self.your_class = your_class

    def work(self):
        # Human.work(self)
        super().work()
        print("I can code")     

boy_1 = Boy(1, "M. Taimur Akhter Sandhu", 9)
# boy_1.work()
# print(boy_1.eyes)
print(boy_1.num_heart)
print(boy_1.name)
print(boy_1.your_class)

print(boy_1.can_breath)
print(Boy.mro())

# End Time : 10 : 56 : 45s PM