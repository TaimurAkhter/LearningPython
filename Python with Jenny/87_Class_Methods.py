# Date: 18th January 2024 Thursday
# Time: 03 : 57 PM
# Time: 04 : 55 PM
# Mama ny aaj kalaf lagwai

# Aaj abu sahiwal gy si foutgi ty

# Start Time: 09 : 19 PM
# End Time: 10 : 02 PM

class Instructor:
    followers = 0   # CLASS OBJECT VARIABLE
    def __init__(self, name, address):
        self.name = name
        self.address = address
        # self.followers = 0
        # self.python = "JavaScript"
    def display(self, python):
        print(f"Hi, I am {self.name} and I am learning {python}.")
    def update_followers(self):
        self.followers += 1
        # print(self.followers)

instructor_1 = Instructor("Taimur", "Gaggoo")
print(instructor_1.name)
# print(instructor_1.followers)
instructor_1.display("Python")
instructor_1.update_followers()
print(instructor_1.followers)

instructor_2 = Instructor("Mamoon", "Gaggoo")
print(instructor_2.followers)
