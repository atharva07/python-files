from random import randint

t = ["Rock","Paper","Scissors"]
computer = t[randint(0,2)]
player = False
comp_result = 0
player_result = 0

while player == False:
    player = input("Rock, Paper, Scissor")
    if player == computer:
        print("Tie")
        print("Computer: {} Player: {}".format(comp_result, player_result))
    elif player == "Rock":
        if computer == "Paper":
            print("You lose", computer, "covers", player)
            comp_result += 1
            print("Computer: {} Player: {}".format(comp_result, player_result))
        else:
            print("You won", player, "smashes", computer)
            player_result += 1
            print("Computer: {} Player: {}".format(comp_result, player_result))
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose", computer, "crushed", player)
            comp_result += 1
            print("Computer: {} Player: {}".format(comp_result, player_result))
        else:
            print("You won", player, "covers", computer)
            player_result += 1
            print("Computer: {} Player: {}".format(comp_result, player_result))
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose", computer, "smashes", player)
            comp_result += 1
            print("Computer: {} Player: {}".format(comp_result, player_result))
        else:
            print("You won", player, "cut", computer)
            player_result += 1
            print("Computer: {} Player: {}".format(comp_result, player_result))
    else:
        print("Its an invalid play, restart game")
        break
        
    player = False
    computer = t[randint(0,2)]