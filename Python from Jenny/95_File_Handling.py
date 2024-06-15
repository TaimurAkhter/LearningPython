# Date: 22th January 2024 Monday
# Time: 06 : 00 PM

# --------------------------Date: 23rd January 2024 Tuesday
# --------------------------Start Time: 06 : 58 PM
# --------------------------End Time: 10 : 52 PM

# 07 : 20 PM Mama Gajryla bna ri wa hn tkriban bn chla wa phir saag pakona wa
# 5 mint pehly mein chaat ty bathal lein gya si mama wi dosry undar gyi si.

# There are two types of files
# Text and Binary

# Some operations on files are:
# open
# read
# write
# close
# These are mainly four operations but there are many more operations as well. 

# How to open the file ?
# First syntax is what use open function, this is in-built function no need to import anything

# Mainly two parameters you need to give
# First is the "filename" then next is "mode"
# open("filename", "mode")

# This open function will return you can say a FileHandler or you can say an Object.
# So that we will store in a variable 
# By default the mode would be considered as read mode

# -----------Read (r) mode-----------         open the file into read mode only.
# It raises error if file doesn't exist. It is default mode for opening files.

# f1 = open("file_1", "r")
# f1_data = f1.read()
# print(f1_data)

# -----------Write mode (w)-----------         open the file into write mode only.
# It overwrites the file if file already exists or create a new file if file doesn't exist. 
# The file Handler exist at the beginning

# f1 = open("file_1", "w")
# f1.write("Date : 23rd January 2024")
# print(f1.read()) # Means we are opening f1 file into write (w) mode so, it will open the file in write mode only. read operator would not be supported.

# -----------Read and Write mode (r+)-----------
# 1. It opens the file in both read and write mode.
# 2. It raises error if file doesn't exist.
# If first you read and then if you write then the file pointer would be at last

# f1 = open("file_1", "r+") # First read then write
# print(f1.read())
# print(f1.tell()) # ----------------It gives position of the File pointer----------
# f1.write("Hi") # The File pointer would be at beginning because you write

# print(f1.tell())
# print(f1.read())
# print(f1.tell()) # The File pointer would be at last because your read

# -----------Write and Read mode (w+)-----------
# 1. It opens the file in both read and write mode.
# 2. The File pointer would be at beginning.
# 3. It overwrites the previous content of the append file if file already exists.
# 4. It creates a new file if no file exists.

# f1 = open("file_1.txt", "w+") # First write then read
# print(f1.tell())
# f1.write("Tomorrow is ")
# print(f1.tell())
# f1.write("Phase 7 Computer and Tarjma-tul-Quran paper")
# print(f1.tell())
# f1.seek(0) # ------------------------We can change the file handler/pointer with seek function
# data = f1.read()
# print(data)
# print(f1.tell())

# f1.close()

# ----------------Append/write mode (a)--------------
# 1. It opens the file in append/write mode.
# 2. The file handler/pointer exists at the end of the previously write in the file if file already exist.
# 3. If file doesn't exist it create a new file
# 4. The newly written data will be added at the end of the file.

# f1 = open("file_1.txt", "a")
# f1.write(" Today is 23rd January 2024 Tuesday")
# print(f1.read()) # Error

# -------------Append/write with read (a+)------------

# ------------Important-------Important-------Important--------while using a or a+ mode-------

# ---------We can't use seek function to change the file handler/pointer position to write text.
# -----We can use seek function to change the file handler/pointer position to read text or piece of text.

# a mode is same as a+
# Difference is a+ mode opens read mode also

# f1 = open("file_1.txt", "a+")
# print(f1.tell())
# f1.seek(0) # ------------------------We can use seek function to change the file handler/pointer position to read text
# print(f1.read())
# f1.write(". Hi")


#----------------------------
# Binary modes : rb, rb+, wb, wb+, ab, ab+ 

# image_1 = open("D:\Pictures\Img20181208123922.jpg", "rb")

# image_2 = open("Mujeeb.jpg", "wb")
# for i in image_1:
#     image_2.write(i)