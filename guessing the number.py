import random

flag= None
Min = int(input("Enter the min number for guessing game: "))
Max = int(input("Enter the max number for guessing game: "))
rand1 = random.randint(Min, Max)
count = 0
best = None
while True:
    if flag == True:
        Min = int(input("Enter the min number for guessing game: "))
        Max = int(input("Enter the max number for guessing game: "))
        rand1 = random.randint(Min, Max)
        print(rand1)
        flag = None
        count=0

    if flag == False:
        print("Good Bye!!!")
        break

    while True:
        num=int(input(f"Guess the number (between {Min} and {Max}): "))

        if num<rand1:
            print("Too low! Try again.")
            count+=1

        elif num>rand1:
            print("Too high! Try again.")
            count+=1

        elif num==rand1:
            if best is None or count < best:
                best = count
            print(f"Congratulations! You guessed the number in {count} attempts.\n Your Lowest Guess record is : {best}")
            if input("Whether you want to play the game? (y/n): ") == "y":
                flag = True
                break
            else:
                flag = False
                break

        if count > 10:
            print("Exceeded Maximum Guesses")
            if input("Whether you want to play the game? (y/n): ") == "y":
                flag = True
                break
            else:
                flag = False
                break
