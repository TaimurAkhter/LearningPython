# Date: 19th January 2024 Friday
# Time: 05 : 09 PM
# Mein ty Abu Badminton khayln Chaat ty gy si.
# Now Time: 05 : 36 PM
# 05 : 36 PM ty Magrab di azan hn hundi pai

# Start writing code Time: 06 : 11 PM

class Employee:
    def __init__(self, name, degree):
        self.name = name
        self.degree = degree

    def eat(self):
        print("I can eat")
    def question(self):
        print("How are you?")
                
class Details:
    def __init__(self, skill):
        self.skill = skill
    
    def flirt(self):
        print("I can flirt")
    def question(self):
        print("What are you doing?")

class Boy(Employee, Details):
    def __init__(self, name, degree, skill):
        Employee.__init__(self, name, degree)
        Details.__init__(self, skill)
    def question(self):
        print("Where are you?")

boy_1 = Boy("Taimur", "None", "HTML,CSS,JS")
# print(Boy.mro()) # Method Resolution Order

print(boy_1.name)
print(boy_1.degree)
print(boy_1.skill)

boy_1.question()      # Where are you?
Details.question(boy_1)  # What are you doing?
