# Date: 20th Dec 2023 Wednesday
# Start Time: 12 : 02 PM
# Start Time: 12 : 32 PM
# Start Time: 12 : 51 PM
import math
def prime_checker(number):
    is_prime = True
    if number==1:
        is_prime = False

    for i in range(2, math.ceil(number/2)+1):
        print("i is:",i)
        
        if number%i == 0:
            is_prime = False

    if is_prime==True:
        print("It is a prime number")
    else:
        print("Not a prime number")
        
            

n = int(input("Enter a number:\n"))
prime_checker(n)

# End Time: 01 : 50 PM   