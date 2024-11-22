#Create a Simple Interest calculator design using python 

principle = 50000

rate = 3

time = 12

simple_interest = (principle * time * rate) /100

print(f"Simple interest amount is : {simple_interest}")

# craete a simple interest calculator design using python user interface 
Amount = int(input("Enter The Ammount : "))

Years = int(input("Enter The numbe Of years : "))

Rate = int(input("Enter The rate Of Interest : "))

Simple_Interest = (Amount * Years * Rate) / 100

print(f"The Simple Interest Is : {Simple_Interest}")