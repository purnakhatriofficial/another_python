import random

capital_text = ["A", "B", "C", "D","E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "O", "Q", "R","S", "T", "U", "V", "W", "X", "Y", "Z",]

small_text = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

character = ["@", "#", "$", "%", "!", "&", ]

number = ["1", "2", "3", "4", "6", "7", "5", "8", "3", "2", "6", "9", ]

random.shuffle(capital_text)
random.shuffle(small_text)
random.shuffle(character)
random.shuffle(number)

random_password = capital_text[2]+ small_text[3]+ capital_text[1]+ character[2]+ small_text[4]+ number[2]+ number[4] + capital_text[1]+ small_text[4] + character[5]+ number[5]

print(f"Your Random Password is : {random_password}")