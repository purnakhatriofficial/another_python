# This are the some of the VARIBALE 
firts_name ="Purna"
middle_name =  "bahadur "
last_name = "khatri"
phone_number = 9829899069
address ="Banphikot-7, Rukum (West)"
gmail = "purnakhatri630@gmail.com"

print(f"My full address {firts_name} {middle_name} {last_name} {phone_number} {address} {gmail}")



sun_income = 4509
mon_income= 5670
tue_income = 8760
wed_income = 7850
thu_income = 8740
fri_income = 8750
sat_income = 980

print (f"My total income is  one week", sun_income+mon_income+tue_income+wed_income+thu_income+fri_income+sat_income)

glass1 = "Milk"
glass2 = "Water"
glass1, glass2 = glass2, glass1

print(f"glass 1 contains {glass1}")
print(f"glass 2 contains {glass2}")



total_bill_amount = 4590
number_of_people = 3

split_amount_of_bill = total_bill_amount / number_of_people

print(f"Each person will be billed: {split_amount_of_bill}")


my_distance = 25
my_speed = 40

time_hourse = my_distance/my_speed
minutes = time_hourse*60

print(f"Time taken to reach in my office : {minutes} minutes ")



number = 7

squre_number = number*number

print(f"Total squre number is: {squre_number}")


dividend = int(input("Enter the dividend"))
divisor = int(input("Enter the divisor"))

quoitent = dividend//divisor
reminder = dividend%divisor

print(f"The quoitent is : {quoitent}")
print(f"The reminder is : {reminder}")


firs_name = input("Enter your name : ")
middle_name = input("Enter your middle name : ")
last_name = input("Enter your last name :")

full_name = firs_name + "" + middle_name + "" + last_name

print(f"Your full name is : {full_name}")



# Very important variable

name = "Purna Bahadiur Khatri+-+"

age = 65

is_marrid = False

number = 34.6

list = ["Purna", "Hari", "Gambhir", "Dipa"]

fruits = {"Apple", "Banana", "Mango", "Orange", "Graps"}



print(type(name))

print(type(age))

print(type(is_marrid))

print(type(number))

print(type(list))

print(type(fruits))

# odd and even number 
num =  int(input("Enter Your Number"))

if(num %2 ) == 0:
    print(f"{num} is odd")
else:
    print(f"{num} is odd")


your_age = int(input("Enter Your Age:"))

if your_age > 18:
    print(f"{your_age} is your voter age ")

else:
    print(f"{your_age} is not a voter age ")


total_books = 540
average_rating = 5
liberation_name = "Joti Laiberary"
is_open = True
book_name = ["Python Programming", "Web Development", "Software Development ", "Data Analytics", "History of Art", "introduction of C&C+"]
location = (456.09, 123.05)
contact_details = {
    "Phone": "+977 9829839069",
    "gamil": "purnakhatri630@gmail.com",
    "address": "456.09 sports city"
}
print(f"Liberarry Information")
print(f"Total number of books : {total_books}")
print(f"Average book ratig: {average_rating}")
print(f"Liberations Name : {liberation_name}")
print(f"Is Liberary open ? : {'Yes' if is_open else 'No'}")
print(f"List of Book name : {book_name}")
print(f"Location is : {location}")
print(f"Contact details : {contact_details}")

print(f"Thank you Everyone visit our liberary ......")





#oPERSTOR 

number1 = 50
number2 = 10

additional = number1+number2
subtraction = number1 - number2
multiplicatio = number2 * number1
division = number1/number2
floor_division = number1//number2
modulus = number1 % number2
exponetiation = number1 ** number2

#Displya Result

print(f"Addition: {number1}+{number2} = {additional}")
print(f"Subtraction: {number1} - {number2} = {subtraction}")
print(f"Multiplication: {number1} * {number2} = {multiplicatio}")
print(f"Division: {number1} / {number2} = {division}")
print(f"Floor Division : {number1} // {number2} = {floor_division}")
print(f"Modules: {number1} % {number2} = {modulus}")
print(f"Expentiation : {number1}**{number2} = {exponetiation}" )

print(f"Thank You Everyone Looks At This Code ")

monthly_expenses = [1504, 2563, 326, 3610, 4560, 3640, 6352,3651, 5698, 4650, 4780, 4650]
tota_spent = sum(monthly_expenses)
average_spent = tota_spent / len(monthly_expenses)
print(f"Total speant in the year {tota_spent}")
print(f" Average monthely spending {average_spent}")




