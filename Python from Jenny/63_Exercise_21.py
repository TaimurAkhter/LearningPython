# Date: 20th Dec 2023 Wednesday
# Start Time: 11 : 47 AM

# You are going to paint a wall. 
# You have to calculate the number of cans of paint needed to paint that complete wall.

import math
# coverage => 1can = 7 sq.meter

def paint_calculation(height, width, cover):
    area = height * width
    no_of_cans = math.ceil(area/cover)
    print(f"You will need {no_of_cans} cans of paint.")

h = int(input("Enter the height of wall in meters:\n"))
w = int(input("Enter the width of wall in meters:\n"))
c = 7

paint_calculation(height=h, width=w, cover=c)

# End Time: 12 : 02 PM