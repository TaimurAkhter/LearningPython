# factorial(7) = 7*6*5*4*3*2*1
# factorial(6) = 6*5*4*3*2*1
# factorial(5) = 5*4*3*2*1
# factorial(4) = 4*3*2*1
# factorial(0) = 1

# factorial(n) = n * factorial(n-1)
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))
# 5 * factorial(4)
# 5 * 4 * factorial(3)
# 5 * 4 * 3 factorial(2)
# 5 * 4 * 3 * 2 factorial(1)
# 5 * 4 * 3 * 2 * 1

# Quick Quiz: Write a program to print the Fibonacci sequence
# f(0) = 0
# f(1) = 1
# f(2) = f(1) + f(2)
# f(3) = f(n-1) + f(n-2)
# f(n) = f(n-1) + f(n-2)
# f(n) = f(n-1) + f(n-2)

# 0 1 1 2 3 5 8 13 21....

# def fi(n):
#     a = 0
#     b = 1
#     if n == 1:
#         print(a)
#     else:
#         print(a)
#         print(b)

#         for i in range(2,n):
#             c = a+b
#             a = b
#             b = c
#             print(b)
# take = int(input("Enter a Number : "))
# fi(take)

def fibonacci(i):
    if i == 0:
        return 0
    elif i == 1:
        return 1
    else:
        return fibonacci(i - 2) + fibonacci(i - 1)
for num in range(15):
    print(fibonacci(num))


'''
fibonacci(2) 0+1 = 1
fibonacci(3) 1+2 = 2
'''