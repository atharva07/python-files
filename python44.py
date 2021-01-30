name = input("Enter your good name = ")
age = int(input("Enter the age = "))
print("Hello", name, " you are", age, " years old")

health = 20

if age >= 18:
    print("You are eligible to play game...")

    want_to_play = input("Do you want to play [yes/no] = ").lower()
    if want_to_play == "yes":
        print("cool lets play.......")
    else:
        print("fine byeeeeeee")
else:
    print("good bye, see you next time")
    