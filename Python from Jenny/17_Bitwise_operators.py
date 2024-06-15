# 28th Oct 2023 Saturday
# Time 6 : 02 PM 
# Now After all Time : 9 : 35 PM

# Date: 26th February 2024 Monday
# End Time 06 : 23 PM
# Aaj Asi Sharif Town gaye si othay Arslan aya si. Ony Awais bahi da WhatsApp number lya si.
# Today I add content in all print statements for clear understanding

"""
Bitwise operators
& and
| or
^ xor
~ not comparison
<< left shift
>> right shift

&, |, ^, ~, <<, >>
and, or, xor, not (comparison), left shift, right shift
"""
print("--------Bitwise Operators--------")

a,b = 5,4
# ---bitwise and operator: & ---
"""
It will give 1 if both are 1, otherwise 0
a = 0101
b = 0100
a&b = 0100
Convert 0100 into decimal. Answer would be 4
"""
print(f"    &  and   a&b : {a & b}")

# ----bitwise or operator: | ----
"""
It will give 0 if both are zero, if anyone is 1 It will give you 1
a    = 0101
b    = 0100
a & b = 0101
Convert 0101 into decimal. Answer would be 5
"""
print(f"    |  or    a|b : {a | b}")

# ----bitwise xor operator: ^ -----
"""
It will give 0 if both are same, if both different It will give you 1
a     = 0101
b     = 0100
a & b = 0001
Convert 0001 into decimal. Answer would be 1
"""
print(f"    ^  xor   a^b : {a ^ b}")

# ----bitwise not operator: ~ ----
a = 6
"""
a = 6
~a will give you -7
Formula: -(n+1)
~a = -(6+1) = -7
"""
print(f"    ~  not   ~a  : {~a}")

# ----bitwise left shift operator: << -----
# In left shift we gain bits we don't lose
a = 5
"""
5 = 0101
5<<2  = 010100
32 16 8 4 2 1
0 1  0 1 0 0 Answer is 20

Simply the formula is what
X<<n calculated as X*(2^n)      (The ^ represents power for better understanding)
5* (2^2) = 5*4 , Answer is 20
"""
print(f"    << left  a<<2 : {a<<2}")

# ----bitwise right shift operator: >> -----
# In right shift we will discard the bits means we are going to the bits
a = 5
"""
5 = 0101
5>>2  = 0001
8 4 2 1
0 0 0 1 Answer is 1

Simply the formula is what
X>>n calculated as X/(2^n)      (The ^ represents power for better understanding)
5/ (2^2) = 5/4 , Answer is 1
"""
print(f"    >> right a>>2 : {a>>2}")