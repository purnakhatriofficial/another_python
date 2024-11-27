first_number = int(input("Enter the first number :"))
second_number =int(input("Enter the second number :"))
third_number = int(input("Enter the third number"))

total_sum = (first_number) + (second_number) + (third_number)

if total_sum > 50:
    print(f"the sum is {total_sum}, which is grater than 50.")
    print(f"The triple of the sum is : {3 * total_sum}")

else:
    print(f"the sum is {total_sum}, which not grater than 50.")