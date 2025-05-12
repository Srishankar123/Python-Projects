import random

randamize_comp_decision=0
def rps(user):
    ob = ["r", "p", "s"]
    if randamize_comp_decision==0:
        comp = random.choice(ob)

    if user == "r":
        print("You chose 🪨")
        if comp == "p":
            print("Computer chose ✋")
            print("You lose!")
        elif comp == "s":
            print("Computer chose ✌")
            print("You win!")
        else:
            print("Computer chose 🪨")
            print("It's a tie!")

    elif user == "p":
        print("You chose ✋")
        if comp == "s":
            print("Computer chose ✌")
            print("You lose!")
        elif comp == "r":
            print("Computer chose 🪨")
            print("You win!")
        else:
            print("Computer chose ✋")
            print("It's a tie!")

    elif user == "s":
        print("You chose ✌")
        if comp == "r":
            print("Computer chose 🪨")
            print("You lose!")
        elif comp == "p":
            print("Computer chose ✋")
            print("You win!")
        else:
            print("Computer chose ✌")
            print("It's a tie!")

while True:
    user = input("Rock, paper, scissor? (r/p/s): ").lower()
    if user not in ["r", "p", "s"]:
        print("Invalid choice!")
        continue

    rps(user)

    user2 = input("Continue? (y/n): ").lower()
    if user2 != "y":
        print("Exiting....")
        break
