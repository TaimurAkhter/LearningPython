# 31st Oct 2023 Tuesday
# Time : 10 : 02 PM

# TRUE LOVE
name1 = input("What is your name?").lower()
name2 = input("What is his/her name?").lower()
combine_string = name1 + name2
lower_case_string = combine_string.lower()

# n1_T, n1_R, n1_U, n1_E = name1.count("t"),name1.count("r"),name1.count("u"),name1.count("e")
# n2_L, n2_O, n2_V, n2_E = name1.count("l"),name1.count("o"),name1.count("v"),name1.count("e")

# n3_T, n3_R, n3_U, n3_E = name2.count("t"),name2.count("r"),name2.count("u"),name2.count("e")
# n4_L, n4_O, n4_V, n4_E = name2.count("l"),name2.count("o"),name2.count("v"),name2.count("e")

# t = n1_T + n3_T
# r = n1_R + n3_R
# u = n1_U + n3_U
# e = n1_E + n3_E

t = lower_case_string.count("t")
r = lower_case_string.count("r")
u = lower_case_string.count("u")
e = lower_case_string.count("e")

true = t + r + u + e

# l = n2_L + n4_L
# o = n2_O + n4_O
# v = n2_V + n4_V
# e = n2_E + n4_E

l = lower_case_string.count("l")
o = lower_case_string.count("o")
v = lower_case_string.count("v")
e = lower_case_string.count("e")

love = l + o + v + e

love_score = int(str(true) + str(love))

if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score} and you go together like coke and mentos")
elif love_score >= 40 or love_score <= 50:
    print(f"Your score is {love_score} and you alright together")    
else:
    print(f"Your score is {love_score}")    