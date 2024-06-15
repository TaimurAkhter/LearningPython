# Date: 20th February 2024 Tuesday
# Start Time: 01 : 26 PM
# End Time: 02 : 31 PM

"""
1. Create a new file "practice.txt" using python. Add the following data in it:
    Hi everyone
    we are learning File 1/0
    using Java.
    like programming in Java.

2. Write a function that replace all occurrences of "Java" with "Python" in above file.

3. Search if the word "learning" exists in the file or not.
"""
# -------1-------
# with open("practice.txt", "w") as f:
#     f.write("Hi everyone\nwe are learning File I/O\n")
#     f.write("using Java.\nI like programming in Java.")

# ------2-------
# with open("practice.txt", "r") as f:
#     data = f.read()

# new_data = data.replace("Java", "Python") # This is a string function remember
# print(new_data)

# with open("practice.txt", "w") as f:
#    f.write(new_data)

# -------3-------
# def check_for_word():
#     word = "learning"
#     with open("practice.txt", "r") as f:
#         data = f.read()
#         if data.find(word) != -1:
#             print("Found")
#         else:
#             print("not found")
# check_for_word()

"""
                            Let's Practice
1. WAF to find in which line of the file does the word "learning" occur first.
Print -1 if word not found.

2. From a file containing numbers separated by comma, print the count of even numbers.
    1, 2, 76, 84, 90, 101
    i) individual number
    ii) parse / casting for int
"""

# ---------1----------
# def check_for_line():
#     word = "learning"
#     line_no = 1
#     with open("practice.txt", "r") as f:
#         while True:
#             data = f.readline()
#             if word in data:
#                 print(line_no)
#                 return
#             line_no += 1
#     return -1
# print(check_for_line())

# ---------2----------
count = 0 
with open("practice.txt", "r") as f:
    data = f.read()
    print(data)

    num = data.split(",")
    print(num)
    for val in num:
        if int(val) % 2 == 0:
            count += 1
print(count)
        

    # without split method
    # num = ""
    # for i in range(len(data)):
    #     if data[i] == ',':
    #         print(int(num))
    #         num = ""
    #     else:
    #         num += data[i]
            

       