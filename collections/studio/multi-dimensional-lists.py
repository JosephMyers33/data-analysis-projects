food = "water bottles,meal packs,snacks,chocolate"
equipment = "space suits,jet packs,tool belts,thermal detonators"
pets = "parrots,cats,moose,alien eggs"
sleep_aids = "blankets,pillows,eyepatches,alarm clocks"

# a) Use split to convert the strings into four cabinet lists. Alphabetize the contents of each cabinet.
food_cabinet = food.split(",")
equipment_cabinet = equipment.split(",")
pets_cabinet = pets.split(",")
sleep_aids_cabinet = sleep_aids.split(',')
# b) Initialize a cargo_hold list and add the cabinet lists to it. Print cargo_hold to verify its structure.
cargo_hold = [food_cabinet,equipment_cabinet,pets_cabinet,sleep_aids_cabinet]
print(cargo_hold)

# c) Query the user to select a cabinet (0 - 3) in the cargo_hold.
user_input = int(input("Please select between 0-3:"))


# d) Use bracket notation and format to display the contents of the selected cabinet. If the user entered an invalid number, print an error message.
if user_input < 4 and user_input > -1:
    print(cargo_hold[user_input])
else:
    print("This is not range of numbers.")



# e) Modify the code to query the user for BOTH a cabinet in cargo_hold AND a particular item. Use the in method to check if the cabinet contains the selected item, then print “Cabinet ____ DOES/DOES NOT contain ____.”
user_item = input("What item are you looking for?")
if user_input < 4 and user_input > -1: 
    if user_item in cargo_hold[user_input]:
        print(f"Cabinet {user_input} DOES contain {user_item}.")
    else:
        print(f"Cabinet {user_index} DOES NOT contain {user_item}.")