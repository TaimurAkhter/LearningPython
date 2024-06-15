# Date: 22th January 2024 Monday

# Date: 25th January 2024 Thursday
# Start Time: 03 : 45 PM
# End Time: 05 : 50 PM --------------Lagatar

# If you store questions and options in a separate file quiz_database.py
# from quiz_database import question_bank
# from quiz_database import options

question_bank = [
    {"text" : "Now in 2024 Who is the most popular Leader in Pakistan?", "answer" : "A"},
    {"text" : "King of fruits?", "answer" : "C"},
    {"text" : "Pakistan is situated in?", "answer" : "D"}
]
options = [
    ["A. Imran Khan", "B. Nawaz Sharif", "C. Zardari", "D. Shahbaz Sharif"],
    ["A. Apple", "B. Banana", "C. Mango", "D. Orange"],
    ["A. Europe", "B. South America", "C. North America", "D. Asia"],
]

print("Welcome to Quiz Game")
score = 0
def check_answer(user_guess, correct_answer):
    if user_guess == correct_answer:
        return True
    else:
        return False

for question_num in range(len(question_bank)): # 0 1 2 3 4
    print(question_bank[question_num]["text"])

    for i in options[question_num]:
        print(i)
        
    guess = input("Enter your answer(A/B/C/D): ").upper()
    is_correct = check_answer(guess, question_bank[question_num]["answer"])
    if is_correct:
        print("Correct Answer")
        score += 1
    else:
        print("Incorrect Answer")
        print(f"The correct answer is {question_bank[question_num]['answer']}")
    print(f"Your current score is {score}/{question_num+1}")
    
print(f"You have given {score} correct answers")
print(f"Your score is {(score/len(question_bank))*100}%")
