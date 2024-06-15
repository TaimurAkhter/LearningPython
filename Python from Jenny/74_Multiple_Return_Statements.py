# Date: 5th January 2024 Friday
# Time: 09 : 49 PM 
# Start Time: 10 : 03 PM 

# import statistics
# def mean_median_mode(list1):
#     return statistics.mean(list1),statistics.median(list1),statistics.mode(list1)

# result = mean_median_mode([3,5,7])
# print(result)
# a,b,c = mean_median_mode([1,2,3])
# print(f"Mean is {a}\nMedian is {b}\nMode is {c}")

def add(a,b):
    if a==0 and b==0:
        return "You have entered zero for both values."
    else:
        return a+b

var1 = int(input("Enter first value:\n"))
var2 = int(input("Enter second value:\n"))
result = add(var1, var2)
print(result)