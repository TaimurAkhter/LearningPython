###----------Today is 3rd February 2024 Saturday And I am Revising CodeWithHarry Concepts.and
###----------Today till now I watch 13 videos. 2024 Elections held on (8th February Thursday)

# --------------------Strings are Immutable

# 25/06/2023 --------------25th June 2023 Sunday
# a = "Tamoor Akhter Sandhu"
# print(len(a)) 
# print(a.upper())
# print(a.lower())
# print(a.split(" ")) # Where there it finds (space or anything you can pass) It separates the words and convert it into a list.
# print(a.replace("Tamoor", "Awais"))

# b = "Jutt!!!!!!Jutt!!!!!!!"
# print(b.rstrip("!")) # remove only last repeating characters

# c = "hOw are you?"
# print(c.capitalize())

# name = "Tamoor !!!! Tamoor !!!"
# print(name.center(50))
# print(len(name))
# print(len(name.center(50)))

# print(name.count("Tamoor"))
# print(name.endswith("!"))

# str1 = "Tamoor and Rahique are Cousin" # 29 length
# print(str1.endswith("Rahique", 0 , 18))

# 26/06/2023 --------------26th June 2023 Monday

str1 = "Taimur, Mamoon and Awais are Brothers"
print(str1.find("Mamoon"))  # If wrong : returns -1

print(str1.index("Awais"))  # If wrong : returns error

str1 = "EidIsComingOn29June2023"
print(str1.isalnum()) # Checking the string contains --only-- A-Z, a-z, 0-9

str1 = "HiComputer"
print(str1.isalpha()) # Checking the string contains --only-- A-Z, a-z

str1 = "hello world"
print(str1.islower())

# Do not use escape sequence characters like \n etc.. while using isprintable() function
str1 = "Cat is running"
print(str1.isprintable()) # True
str1 = "Cat is running\n"
print(str1.isprintable()) # False

str1 = "      "
print(str1.isspace()) # It returns True if the string --only-- contains white spaces

str1 = "World Health Organization"
print(str1.istitle()) # True

str1 = "LooK likE honeY"
print(str1.startswith("LooK"))

print(str1.istitle()) # It checks that first letter of each word is capital
print(str1.title()) # It converts the first letter of each word capital.

print(str1.swapcase()) # It converts lowercase letter into uppercase and uppercase letter into lowercase.

###----------Today is 3rd February 2024 Saturday 
# Now after writing the descriptions of string methods
# End Time : 09 : 43 PM