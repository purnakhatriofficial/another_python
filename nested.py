start_number = int(input("Please Enter Your Start number : "))
end_number   = int(input("Please Enter Yor End Number :  "))

for i in range(start_number, end_number+1):
    for j in range (1,11):
        print(f"{i} * {j} = {i * j}")
    print("\n")