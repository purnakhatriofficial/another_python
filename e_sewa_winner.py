#Write a generation of lucky e_sewa car winner Number 2024
import random

customer_name = ["Purna Bahadur Khatri", "Ram Khatr", "Paras Paudel", "Sumit Nepal", "Tika Khatri", "Dipa Oli", "Laxamn Oli"]
customer_number = ["982983******", "98563595***", "98635895***", "9856895***", "9856895***", "98456895***", "984566895***", "98458895***","98456895***",]

customer_lucky_index = random.randint(0, len(customer_number) -1)

print(f"Congratulation {customer_name[customer_lucky_index]}! E-sewa Iphone-16 Winner in 2024 Your number is {customer_number[customer_lucky_index]} Please receive your gift ")