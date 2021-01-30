dict = {} 
# stores name and birth date
while True:
    print("-----------birthday-----------")
    print("1. Show Birthday")
    print("2. Add to Birthday list")
    print("3. Exit")
    choice = int(input("Enter the choice = "))
    if choice == 1:
        if len(dict.keys()) == 0:
            print("Nothing to show")
        else:
            name = input("Enter the name to search = ")
            birthday = dict.get(name, "No data found")
            print(birthday)
    elif choice == 2:
        name = input("Enter the friends name = ")
        data = input("Enter birth date = ")
        print("Birthday added")
    elif choice == 3:
        break
    else:
        print("Invalid option")