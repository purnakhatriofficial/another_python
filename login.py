#login password


user_name = "Purnakhatri12"
user_password = "Purna@#$123"


user_input = input(f"Enter User Name :")
input_password = input(f"Enter Your Password :")

if user_name == user_input and user_password == input_password:
    print(f"Your Password Login Successful ")
else:
        print(f"Incorrect Your Password")