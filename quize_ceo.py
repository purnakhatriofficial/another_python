print("Welcome To the Quiz Game! ❤️❤️")
print("Answer the following questions 😎😎")

# Question and Answer Store
question_number_one = "1. Who is the CEO of Facebook?"
answer_one = "Mark Zuckerberg"

question_number_two = "2. Who is the CEO of Tesla?"
answer_two = "Elon Musk"

question_number_three = "3. Who is the CEO of Microsoft?"
answer_three = "Satya Nadella"

question_number_four = "4. Who is the CEO of Netflix?"
answer_four = "Ted Sarandos and Greg Peters"

question_number_five = "5. Who is the CEO of Apple?"
answer_five = "Tim Cook"

question_number_six = "6. Who is the CEO of Samsung?"
answer_six = "Han Jong-hee"

question_number_seven = "7. Who is the CEO of YouTube?"
answer_seven = "Neal Mohan"

question_number_eight = "8. Who is the CEO of Amazon?"
answer_eight = "Andy Jassy"

question_number_nine = "9. Who is the CEO of Google?"
answer_nine = "Sundar Pichai"

question_number_ten = "10. Who is the CEO of Yelp?"
answer_ten = "Jeremy Stoppelman"

# Score store
score = 0

# Question Number 1
print("\n" + question_number_one)
user_answer_one = input("Your Answer: ").strip()
if user_answer_one.capitalize() == answer_one.capitalize():
    print("Correct!")
    score += 1
else:
    print(f"Wrong! The correct answer is: {answer_one}")

# Question Number 2
print("\n" + question_number_two)
user_answer_two = input("Your Answer: ").strip()
if user_answer_two.capitalize() == answer_two.capitalize():
    print("Correct!")
    score += 1
else:
    print(f"Wrong! The correct answer is: {answer_two}")

# Question Number 3
print("\n" + question_number_three)
user_answer_three = input("Your Answer: ").strip()
if user_answer_three.capitalize() == answer_three.capitalize():
    print("Correct!")
    score += 1
else:
    print(f"Wrong! The correct answer is: {answer_three}")

# Question Number 4
print("\n" + question_number_four)
user_answer_four = input("Your Answer: ").strip()
if user_answer_four.capitalize() == answer_four.capitalize():
    print("Correct!")
    score += 1
else:
    print(f"Wrong! The correct answer is: {answer_four}")

# Question Number 5
print("\n" + question_number_five)
user_answer_five = input("Your Answer: ").strip()
if user_answer_five.capitalize() == answer_five.capitalize():
    print("Correct!")
    score += 1
else:
    print(f"Wrong! The correct answer is: {answer_five}")

# Question Number 6
print("\n" + question_number_six)
user_answer_six = input("Your Answer: ").strip()
if user_answer_six.capitalize() == answer_six.capitalize():
    print("Correct!")
    score += 1
else:
    print(f"Wrong! The correct answer is: {answer_six}")

# Question Number 7
print("\n" + question_number_seven)
user_answer_seven = input("Your Answer: ").strip()
if user_answer_seven.capitalize() == answer_seven.capitalize():
    print("Correct!")
    score += 1
else:
    print(f"Wrong! The correct answer is: {answer_seven}")

# Question Number 8
print("\n" + question_number_eight)
user_answer_eight = input("Your Answer: ").strip()
if user_answer_eight.capitalize() == answer_eight.capitalize():
    print("Correct!")
    score += 1
else:
    print(f"Wrong! The correct answer is: {answer_eight}")

# Question Number 9
print("\n" + question_number_nine)
user_answer_nine = input("Your Answer: ").strip()
if user_answer_nine.capitalize() == answer_nine.capitalize():
    print("Correct!")
    score += 1
else:
    print(f"Wrong! The correct answer is: {answer_nine}")

# Question Number 10
print("\n" + question_number_ten)
user_answer_ten = input("Your Answer: ").strip()
if user_answer_ten.capitalize() == answer_ten.capitalize():
    print("Correct!")
    score += 1
else:
    print(f"Wrong! The correct answer is: {answer_ten}")

# Final Score
print(f"\nYour final score is: {score}/10")
if score == 10:
    print("Excellent! You are a quiz master 😘😊")
elif score >= 5:
    print("Good job! You passed the quiz 😊")
else:
    print("Better luck next time. Keep practicing ❌❌❌")
