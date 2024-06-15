# Date: 6th January 2024 Saturday
# Start Time: 09 : 36 PM
# End Time: 09 : 45 PM
a = 10 # global
def display():
    # a = 15 # local
    def show():
        print(a)
    show()
display()

# In python there is no block scope
a,b = 4,5
if a<b:
    c=a+b
print(c)