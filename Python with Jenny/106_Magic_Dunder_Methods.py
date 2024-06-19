# Date: 5th February 2024 Monday

# ------Start Time : 09 : 20 PM
#----------End Time: 11 : 07 PM

# Magic Methods allows us to use some builtin operations in python like len,str and many builtin operations are there in python.
# So these Methods allows us to use these builtin operations with our own user created objects like we create class and we create object of that class that is our own user created object so we can use these builtin operations with our own objects.

# list1 = [1, 0, -1]
# print(len(list1))

class Author:
    def __init__(self, name, date, time):
        self.name = name
        self.date = date
        self.time = time
    def __len__(self):
        return 5
    def __str__(self):
        return f"Date: {self.date}\nTime: {self.time}"
    def __call__(self, *args, **kwargs):
        print(f"{self.name}")
    def __del__(self):
        print("Author object has been deleted")   
        
d = Author("Awais", "5th February 2024 Monday", "10 : 59 PM")
print(len(d))
print(d)
d()

del d
# print(d)
