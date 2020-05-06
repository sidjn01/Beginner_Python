choice = 5

while choice != 0:
    print("Please choose from the following options")
    print("1.   Learn Python")
    print("2.   Learn Java")
    print("3.   Go swimming")
    print("4.   Have dinner")
    print("0.   Exit")
    choice = int(input())

    if choice == 1:
        print("Python")
    elif choice == 2:
        print("Java")
    elif choice == 3:
        print("Swim")
    elif choice == 4:
        print("Dinner")
    elif choice == 0:
        print("Program Exited")
        break
    else:
        print("Enter valid choice")

