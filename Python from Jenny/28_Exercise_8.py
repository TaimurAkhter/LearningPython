# 31st Oct 2023 Tuesday
# Completed Time : 02 : 34 PM

year = int(input("Enter year:"))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year")
        else:
            print("Not Leap year")
    else:
        print("Leap year")
else:
    print("Not Leap year")

# Check the year 1900,1700,1500 etc...
# 1900 is divisible by 4 and divisible by 100, but not divisible by 400 So, It is not Leap year