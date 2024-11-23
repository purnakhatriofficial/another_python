
light = ["On", "Off"]

current_light = input("Please Enter the light : ").capitalize()

if current_light == 'On':
    print(f"Light On")
elif current_light == 'Off':
    print(f"Light Off")
else:
    print(f"Light Damage ")