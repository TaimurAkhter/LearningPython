# Date: 27th January 2024 Saturday
# Start Time: 04 : 33 PM
# End Time: 04 : 56 PM

# 1.
import my_module
print(my_module.location)
print(my_module.sum(3,5))

# 2. Rename the module name using (as) keyword
# import my_module as my
# print(my.date())
# print(my.name)

# 3. To import direct things we use (from) keyword
# from my_module import name, date
# print(date())
# print(name)
# print(location) # Error : NameError: name 'location' is not defined

# 4. To import all things directly from own created module we use (*) keyword after (import) keyword
# from my_module import *
# print(date())
# print(name)
# print(location)

# We can use (as) to rename one thing only while using (from) keyword like name or location.
# from my_module import name as n
# print(n)