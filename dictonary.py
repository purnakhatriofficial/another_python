#Dictonary 

Country_capatial = {
    "Nepal": "Kathmandu",
    "India": "Delhi",
    "USA": "New York",
    "China": "Beigung"
}

#Accessing a Value

print(Country_capatial["Nepal"])

#Add Value

Country_capatial["Japan"] ="Tokiyo"
Country_capatial["Australia"] = "Canberra"
Country_capatial["Canada"] = "Ottawa"

#Update Values 

Country_capatial["China"] ="Beijing"

#Delet Value

del Country_capatial["China"]


# printing the Dictonary 

print(f"The all country captial is : {Country_capatial}")