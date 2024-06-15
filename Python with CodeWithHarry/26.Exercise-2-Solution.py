###----------Today is 4th February 2024 Sunday 
###----------Start Coding Time 06 : 46 PM

import time

t = time.strftime('%H:%M:%S')
hour = int(time.strftime('%H'))
hour = int(input("Enter hour: "))
print(hour)

if (hour>=0 and hour<12):
    print("Good Morning Sir!")
elif (hour>=12 and hour<17):
    print("Good Noon Sir!")  
elif (hour>=17 and hour<0):
    print("Good Night Sir!")

###------End Time: 06 : 48 PM