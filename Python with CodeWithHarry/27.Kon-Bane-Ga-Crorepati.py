questions = [
    [
        "Pakistan's most popular leader in the History?", "Imran Khan", "Nawaz Sharif", "Shehbaz Sharif", "Bhutto", 1
    ],
    [
        "When did Pakistan gain independence from British rule?", "1945", "1947", "1950", "1955",2
    ],
    [
        "When did Pakistan become a republic?", "1947", "1956", "1971", "1973", 2
    ],
    [
        "Who was the first Governor-General of Pakistan?", "Muhammad Ali Jinnah", "Liaquat Ali Khan", "Ayub Khan", "None", 1
    ],
    [
        "In 14th July 2023 which political leader is Popular in Pakistan?", "Shehbaz Sharif", "Nawaz Sharif", "Imran Khan","Bilawal Bhutto", 3
    ],
    [
        "Capital of Pakistan in 2023?", "Islamabad", "Lahore", "Karachi", "None", 1
    ],
    [
        "Which language was used to create this Program?", "Python", "JavaScript", "Php", "None", 1
    ]
]

levels = [50000, 100000, 300000, 500000, 700000, 900000, 1000000]
money = 0

for i in range(0, len(questions)):
    question = questions[i]
    print(f"\n\nQuestion for RS. {levels[i]} ")
    print(f"{question[0]}")
    print(f"a. {question[1]}        b. {question[2]}")
    print(f"c. {question[3]}        d. {question[4]}")
    reply = int(input("Enter your answer (1-4) or 0 to quit"))
    if (reply == 0):
        money = levels[i-1]
        break
    if (reply == question[-1]):
        print(f"Correct answer, you have won Rs. {levels[i]}")
    else:
        print("Wrong Answer!")
        print(f"Your take home money is {money}")
        break


