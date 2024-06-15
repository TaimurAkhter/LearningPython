# Date: 26th February 2024 Monday
# Time 06 : 25 PM
# Aaj Asi Sharif Town gaye si othay Arslan aya si. Ony Awais bahi da WhatsApp number lya si.

# Start Time 07 : 47 PM
# Now I work on logic building
# ------Now I am start creating a program to find HCF of two numbers own my own

# Date: 26th February 2024 Monday
# Time 09 : 02 PM Awais bahi naal gaal kiti hn o Gadafi Stadium Lahore PSL da Match dekhn gya pehli waaar Awaaza andia si ty samaj nahi lagdi si phr call bnd krti

# End Time 10 : 25 PM AAJ mein time waste kita HCF FIND KRN TY mein pehly factor nikalan ch nakaam rya phr solution hn wekhya


# Hn 10 :  29 PM ty codewithharry da small ja solution wekh ky mein hyraan rah gya
num1 = int(input("Enter 1st number\n"))
num2 = int(input("Enter 2nd number\n"))

if num2 > num1:
    mn = num1
else:
    mn = num2

for i in range(1, mn+1):
    if num1%i == 0 and num2%i == 0:
        hcf = i

print(f"The HCF/GCD of these two numbers is {hcf}")

# --------------LCM
a = int(input("Enter 1st number\n"))
b = int(input("Enter 2nd number\n"))

maxNum = max(a, b)

while True:
    if maxNum%a == 0 and maxNum%b == 0:
        break
    maxNum += 1

print(f"The LCM of {a} and {b} is {maxNum}")

# End Time 10 : 39 PM

# Aaj mein Jenny waly python dy folder ch bitwise operator nu set kita

# End Time 10 : 40 PM