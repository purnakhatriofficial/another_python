

print("Welcome To the Quiz Game!")

print("Answer The Following Questions")

# Questions and Answers Store
question_number_one = "1. Where is the capital of Nepal?"
answer_one = "Kathmandu"

question_number_two = "2. Who is the Prime Minister of Nepal?"
answer_two = "KP Sharma Oli"

question_number_three = "3. Who is the Education Minister of Nepal?"
answer_three = "Bidhya Bhattrai"

question_number_four = "4. Who is the Minister of Information and Communication of Nepal?"
answer_four = "Prithvi Subba Gurung"

question_number_five = "5. Who is the President of Nepal?"
answer_five = "Ram Chandra Paudel"

# Score
score = 0

# Question Number 1
print("\n" + question_number_one)
user_answer_one = input("Your Answer: ").strip()
if user_answer_one.capitalize() == answer_one.capitalize():
    print("Correct!")
    score += 1
else:
    print(f"Wrong! The Correct Answer is: {answer_one}")

# Question Number 2
print("\n" + question_number_two)
user_answer_two = input("Your Answer: ").strip()
if user_answer_two.capitalize() == answer_two.capitalize():
    print("Correct!")
    score += 1
else:
    print(f"Wrong! The Correct Answer is: {answer_two}")

# Question Number 3
print("\n" + question_number_three)
user_answer_three = input("Your Answer: ").strip()
if user_answer_three.capitalize() == answer_three.capitalize():  # Fixed the logic here
    print("Correct!")
    score += 1
else:
    print(f"Wrong! The Correct Answer is: {answer_three}")

# Question Number 4
print("\n" + question_number_four)
user_answer_four = input("Your Answer: ").strip()
if user_answer_four.capitalize() == answer_four.capitalize():  # Added parentheses to .capitalize()
    print("Correct!")
    score += 1
else:
    print(f"Wrong! The Correct Answer is: {answer_four}")

# Question Number 5
print("\n" + question_number_five)
user_answer_five = input("Your Answer: ").strip()
if user_answer_five.capitalize() == answer_five.capitalize():  # Added parentheses to .capitalize()
    print("Correct!")
    score += 1
else:
    print(f"Wrong! The Correct Answer is: {answer_five}")

# Final Score
print(f"\nYour final score is: {score}/5")
if score == 5:
    print("Excellent! You are a Quiz Master 😊")
elif score >= 3:
    print("Good job! You passed the quiz 😒")
else:
    print("Better luck next time. Keep practicing 😡❌❌")
