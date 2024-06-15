letter = "Hey my name is {1} and I am from {0}"
city = "Gaggoo Mandi"
name = "Taimur Akhter"

print(letter.format(city, name))
print(f"Hey my name is {name} and I am from {city}")

print(f"Hey my name is {{name}} and I am from {{city}}")

price = 49.62523
txt = f"For only {price:.2f} dollars!" # :.2f means we get two decimal place digit
print(txt)
# print(txt.format())
print(type(f"{2 * 30}"))

country = ["Spain", "Germany", "Finland", "England"]
print(f"List of some countries {country[2]}")


