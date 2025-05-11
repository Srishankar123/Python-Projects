import random

times_y = 0
while True:

    choice = input("Roll the dice? (y/n): ").lower()

    if choice!='y' and choice!='n' :
        print("Invalid choice!")

    elif choice=="y":
        choice1 = int(input("How many dices need to be rolled? "))
        times_y += 1
        result=[]
        while choice1>0:
            rand1 = random.randint(1, 6)
        #rand2 = random.randint(1, 6)
            result.append(rand1)
            choice1-=1

        print(result)

    elif choice=="n":
        print("Thanks for playing!")
        print(times_y)
        break

------------------------------------------------------------------------------------------------------------------

import random

while True:
    choice = input("Roll the dice? (y/n): ")

    if choice != 'y' and choice != 'n':
        print("Invalid choice!")

    elif choice == "y":
        rand1 = random.randint(1, 6)
        rand2 = random.randint(1, 6)
        print(f"({rand1}, {rand2})")

    elif choice == "n":
        print("Thanks for playing!")
        break
