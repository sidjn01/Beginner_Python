name = input("Please enter name:")
age = int(input("How old are you?"))

if 18 <= age < 31:
    print("Welcome to club 18-30 holiday, {}".format(name))

else:
    print("I'm sorry, our holiday are only for cool people")