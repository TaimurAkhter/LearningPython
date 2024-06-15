# Date: 19th Dec 2023 Tuesday
# Start Time: 09 : 31 PM

# There are four types of arguments
# Default (Parameters in the function definition assigned default values.)
# Positional (Values passed to a function based on the order of parameters in the function definition.)
# Keyword (Values passed to a function with the parameter names specified.)
# Arbitrary / variable length

# Arbitrary arguments are of two types
# arbitrary positional arguments
# arbitrary keyword arguments

def greet(name, dept, subject="Python"):
    print(f"Hi {name}")
    print(f"Do you teach {subject}?")
    print(f"Are you from {dept} department?")

# -------Positional arguments---------
# greet("Mamoon", "CS")
    
# -------Keyword arguments---------
# In a function first write positional arguments then keyword arguments.

# greet(dept="CS", name="Mamoon")
# greet("Mamoon", dept="CS")
    
# -------Default arguments---------
# In a function first write non-default arguments then write default arguments.

# greet("Taimur", "AI")

# -------Arbitrary arguments---------
# 1. arbitrary positional arguments

def add(*numbers):
    c = 0
    for i in numbers:
        c += i
    print(f"Sum is {c}")
add(108, 143)    
add(98, 59, 48)    
add(98, 59, 48, 40)

# Date: 20th Dec 2023 Wednesday
# End Time: 10 : 06 AM