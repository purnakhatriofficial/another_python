# Function to determine the season
def get_season(month):
    
    month = month.lower()
    
    if month in ["december", "january", "february", "12", "1", "2"]:
        return "Winter"
    elif month in ["march", "april", "may", "3", "4", "5"]:
        return "Spring"
    elif month in ["june", "july", "august", "6", "7", "8"]:
        return "Summer"
    elif month in ["september", "october", "november", "9", "10", "11"]:
        return "Autumn"
    else:
        return "Invalid input. Please enter a valid month name or number."


user_input = input("Enter the month name or number (e.g., 'March' or '3'): ")


season = get_season(user_input)
print(f"The season is: {season}")
