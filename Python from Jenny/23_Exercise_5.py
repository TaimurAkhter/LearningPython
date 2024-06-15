# 29th Oct 2023 Sunday
# 11 : 46 AM

# Find out how many days, weeks and months we have left if we live until 90 years old
# 1year = 365 days
# 1year = 52 weeks
# 1year = 12 months

age = int(input("Enter your age: "))
# a = (90 * 365) - (age * 365)
# b = (90 * 52) - (age * 52)
# c = (90 * 12) - (age * 12)
# print(f"You have {a} days, {b} weeks and {c} months left.")

years_left = 90-age
days_left = years_left * 365
weeks_left = years_left * 52
months_left = years_left * 12
print(f"You have {days_left} days, {weeks_left} weeks and {months_left} months left.")

# Time 12 : 02 PM