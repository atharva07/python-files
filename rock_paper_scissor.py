# import random module
import random
from random import randint
# print multiline instruction
# performing concatenation of string
print("winning rules of Rock-Paper-Scissor game as follows: \n "
        + "Rock vs Paper -> Paper wins \n"
        + "Rock vs Scissor -> Rock wins \n"
        + "Paper vs Scissor -> Scissor wins \n")

while True:
    print("Enter the choice you want \n 1.Rock \n 2.Paper \n 3.Scissor \n")

    # take the input from the user
    choice = int(input("user turn = "))

    # OR is the short-circuit operator
    # if anyone condition is true
    # Then it will return true value

    while choice > 3 or choice < 1:
        choice = int(input("Enter the choice = "))

        if choice == 1:
            choice_name = 'rock'
        elif choice == 2:
            choice_name = 'Paper'
        else:
            choice_name = 'Scissor'
    
    # print user choice
    print("user choice is = " + choice_name)
    print("\nNow its computer turn.....")

    # computer uses random choice between 1 and 3
    comp_choice = random.randint(1,3)

    # looping until comp_choice is equal to choice
    while comp_choice == choice:
        comp_choice = random.randint(1,3)

    # initializing the values to comp_choice
    if comp_choice == 1:
        comp_choice_name == 'Rock'
    elif comp_choice == 2:
        comp_choice_name == 'Paper'
    else:
        comp_choice_name == 'Scissor'

    print("computer choice is " + comp_choice_name)

    print(choice_name + "V/s" + comp_choice_name)

    # condition for winning 
    if ((choice == 1 and comp_choice == 2) or (choice == 2 and comp_choice == 1)):
        print("Paper wins =>", end = " ") 
        result = "Paper"
    elif ((choice == 1 and comp_choice == 3) or (choice == 3 and comp_choice == 1)):
        print("Rock wins =>", end = " ")
        result = "Rock"
    else:
        print("Scissor wins =>", end = " ")
        result = "Scissor"
    
    # Printing either user or computer wins
    if result == choice_name:
        print("User wins")
    else:
        print("computer wins")
    
    print("Do you want to play again? Y/N")
    ans = input()

    if ans == 'n' or ans == 'N':
        break

print("thanks for playing")
        