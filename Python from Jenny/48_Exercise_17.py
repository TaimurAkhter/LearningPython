# Date: 10 December 2023 Sunday
# Time: 05 : 57 PM
# Today Me and mama went to 205 at 01:30 PM. We came back to home at 04:00 PM.

# FizzBuzz Job Interview Question
# number divisible by 3 => Fizz 
# number divisible by 5 => Buzz
# number divisible by 3 and 5 => FizzBuzz

for i in range(1, 31):
    if i%3 == 0 and i%5 == 0:
        print("FizzBuzz")
    elif i%3 == 0:
        print("Fizz")
    elif i%5 == 0:
        print("Buzz")
    else:
        print(i) 

# End Time: 06 : 17 PM