print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_______/
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
cross_road = input("You're at a cross road. Where do you want to go?\n Type 'left' or 'right'\n").lower()
if cross_road == "left":
    lake = input("You've come to a lake. There is an island in the middle of the lake.\n "
                 "Type 'wait' to wait for a boat. Type 'swim' to swim across.\n").lower()
    print(lake)
    if lake == "swim":
        island = input("You've arrived at the island unharmed. "
                       "There is a house with three doors.\nOne red. one yellow, and one blue. "
                       "Which colour do you choose?\n").lower()
        print(island)
        if island == "yellow":
            print("You win!")
        else:
            print("Wrong choice! Python got you.")
    else:
        print("There's no boat coming. Game over.")
else:
    print("You've been attacked. Game over.")