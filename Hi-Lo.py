low = 1
high = 10

print("Think of a number between {} and {}".format(low, high))
input("Press Enter to start")

guesses = 1

while low != high:
    guess = low + (high-low) // 2
    high_low = input("My guess is {}. Should I guess higher or lower? "
                     "Enter h or l, or c if my guess was correct ".
                     format(guess)).casefold()
    if high_low == "h":
        low = guess + 1

    elif high_low == "l":
        high = guess - 1

    elif high_low == "c":
        print("I got it in {} guesses!".format(guesses))
        break

    else:
        print("Enter h, l or c")

    guesses += 1
else:
    print("You thought of a number {}".format(low))
    print("I got it in {} guesses".format(guesses))