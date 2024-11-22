
#write a code generation you go to resturent with your friend and and order pizza pay bill lucky person

import random

total_bill_amount = 2550

name_of_people = ["Purna", "Sagar", "Hari", "Ram", "Laxman", "Dewa"]

bill_pay_lucky_index = random.randint(0, len(name_of_people) - 1)

print(f"Dear {name_of_people [bill_pay_lucky_index]}, You Have To Pay  The Bill Of Rs: {total_bill_amount} ")