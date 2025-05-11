import random

min=int(input("Enter the min number for guessing game: "))
max=int(input("Enter the max number for guessing game: "))
rand1=random.randint(min,max)
print(rand1)
count=0


while True:
    num=int(input(f"Guess the number (between {min} and {max}): "))

    if num<rand1:
        print("Too low! Try again.")
        count+=1

    elif num>rand1:
        print("Too high! Try again.")
        count+=1

    elif num==rand1:
        print(f"Congratulations! You guessed the number in {count} attempts.")
        break

    if count > 10:
        print("Exceeded Maximum Guesses")
        break

