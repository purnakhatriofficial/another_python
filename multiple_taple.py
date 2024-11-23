start_number = int(input("Enter The Start Number : "))

end_number = int(input("Enter The End Number :   "))

for i in range (start_number, end_number +1):
    for j in range (1,11):
        print(f"{i} * {j} = {i *j}")
print("\n")