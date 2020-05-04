import random

highest = 1000
answer = random.randint(1, highest)

print("Please guess number between 1 and {}:".format(highest))

guess = 0

while guess != answer:
    guess = int(input())

    if guess == 0:
        break
    if guess == answer:
        print("You guessed it right")
        break
    else :
        if answer < guess:
            print("Guess lower")
        else :
            print("Guess higher")