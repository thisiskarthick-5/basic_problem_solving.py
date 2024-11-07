import random

def guess_number():
    number = random.randint(1,100)


    while True:
        guess = int(input("ENTER THE GUESS NUMBER : "))
        if guess<number:
            print("your are too low ")
        elif guess<number:
            print("your are too high")
        else:
            print("correct!")
            break

guess_number()
                