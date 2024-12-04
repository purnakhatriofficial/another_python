def minvoter_age():
    
    return 18

voters = {
    'Purna':23,
    "Dil" :20,
    'Amrit': 19,
    'Kalpan': 12,
    "Hari" : 17,
}

for name, age in voters.items():
    if age >= minvoter_age ():
        print(f"Congratulation {name}, you can vote")
    else:
        print(f"Sorry {name} you can't vote come back after {minvoter_age() - age} years")