answer = 5

print("Please guess number between 1 and 10:")
guess = int(input())

if guess != answer :
    if guess < answer :
        print("Please guess higher")
    else :
        print("Please guess lower")
    guess = int(input())
    if guess == answer :
        print("Well done, you guessed it")
    else :
        print("Sorry, you have not guessed correctly")
else :
    print("You got it the first time")

# LESS EFFICIENT VERSION
# if guess < answer :
#     print("Please guess higher")
#     guess = int(input())
#     if guess == answer :
#         print("Well done, you guessed it")
#     else :
#         print("Sorry,you have not guessed correctly")
#
# elif guess > answer :
#     print("Please guess lower")
#     guess = int(input())
#     if guess == answer :
#         print("Well done you guessed it")
#     else :
#         print("Sorry,you have not guessed correctly")
#
# else :
#     print("You got it first time")

# ANOTHER WAY TO DO THE GAME
# answer = 5
#
# print("Please guess number between 1 and 10:")
# guess = int(input())
#
# if guess == answer :
#     print("You got it the first time")
# else :
#     if guess < answer :
#         print("Please guess higher")
#     else :
#         print("Please guess lower")
#     guess = int(input())
#     if guess == answer :
#         print("Well done, you guessed it")
#     else :
#         print("Sorry, you have not guessed correctly")