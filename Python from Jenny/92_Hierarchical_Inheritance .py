# Create this file on
# Date: 20th January 2024 Saturday
# Time: 11 : 01 PM

# Date: 21th January 2024 Sunday
# Time: 01 : 18 PM
"""
Aaj Abu subha 8:30 wajy da gya Vehari Election training ty. Kal wi jana wa Vehari. Do din di training a.
Mein ty mama bethay si ty mein status wekhya Mis ramzanay di ami foot hogai. Mama nu hn Anti Mussarat dy kaar chad ky aya waaan.  
"""
# Start Time: 01 : 21 PM
# Start code writing Time: 01 : 51 PM
# End Time: 02 : 06 PM

class Human:
    def __init__(self, name, city):
        print("Calling init from human class")
        self.name = name
        self.city = city

    def showDetails(self):
        print(f"My name is {self.name} and I live in {self.city}")        

    def eat(self):
        print("I can eat")
class Male(Human):
    def __init__(self, name, city, support):
        print("Calling init from male class")
        Human.__init__(self, name, city)
        self.support = support

    def sleep(self):
        print("I sleep upto 7 or 8 hours")
class Female(Human):
    def __init__(self, name, city):
        print("Calling init from male class")
        super().__init__(name, city)

    def work(self):
        print("I can code")

female_1 = Female("Salma", "Gaggoo")
female_1.showDetails()

# male_1 = Male("Taimur", "Gaggoo", "Imran Khan")
# male_1.showDetails()
# print(Male.mro())
