daily_expensis = [4556, 4245, 149, 4054, 2454, 2445, 987]

#calculate the total weekly expense

total_expense = sum(daily_expensis)

#calculate the average daily expenses

average_expensis = total_expense / len(daily_expensis  )

#Display the result

print(f"Daily Expense : {daily_expensis}")
print(f"Total wekly expense : {total_expense} " )
print(f"Average expense : {average_expensis}")