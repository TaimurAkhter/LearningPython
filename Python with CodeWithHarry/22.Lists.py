#----------Today is 4th February 2024 Sunday 
###----------Start Time 12 : 16 PM

marks = [3, 5, 6, "Harry", True, 6, 7, 2, 32, 345, 23]
# print(marks)
# print(type(marks))
# print(marks[0])
# print(marks[1])
# print(marks[2])
# print(marks[3])
# print(marks[4])
# print(marks[5])

# print(marks[-3]) # Negative index
# print(marks[len(marks)-3]) # Positive index
# print(marks[5-3]) # Positive index
# print(marks[2]) # Positive index

# if "6" in marks:
#     print("Yes")
# else:
#     print("No")

# Same thing applies for strings as well!
# if "Ha" in "Harry":
#     print("Yes")

# print(marks)
# print(marks[1:9])
# print(marks[1:9:3])

lst = [i*i for i in range(10)]
print(lst)
lst = [i*i for i in range(10) if i%2==0]
print(lst)



# listA = [ 'GameOfThrones ' ,8 , 'StrangerThings', 3,'Friends',10]
# listB =  ['Emilia Clarke' ,'Millie Bobby Brown', 'Jennifer Aniston']
# print(listA)
# print(listB)

# listA = [ 'GameOfThrones ' ,8 , 'StrangerThings', 3,'Friends',10]
# listB =  ['Emilia Clarke' ,'Millie Bobby Brown', 'Jennifer Aniston']
# print("listA[2]: ", listA[2])
# print("listB[1:2]: ", listB[1:2])

# listB =  ['Emilia Clarke' ,'Millie Bobby Brown', 'Jennifer Aniston']
# print("Before change", listB)
# listB[2] = "Emma Mackey"
# print("After change", listB)