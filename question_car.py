class car :

    def __init__(self, id, name, brand):
        self.id = id
        self.name = name
        self.brand = brand

    def display_detail(self):
        print(f"Car Id : {self.id}")
        print(f"Car name : {self.name}")
        print(f"Car Brand : {self.brand}")

car1 = car(1, "Model's", "Tesla")
car1.display_detail()


class Student:
    def __init__(self, name, address, phone):
        self.name = name
        self.address = address
        self.__phone = phone
    
    def get_phone(self):
        return self.__phone
    
    def set_phone(self, phone):
        self.__phone = phone
        
    def display(self):
        print(f"Name is {self.name}, address is {self.address} and phone is {self.__phone}")
# Creating Object [s1]

s1 = Student("", "", "")
s1.name = input("Enter student name: ")
phone = input("Enter phone: ")
s1.set_phone(phone)
s1.address = input("Enter address: ")

s1.display()