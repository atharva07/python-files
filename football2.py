def bubble_sort(array):
    for i in range(len(array)):
        swapped = True
        for j in range(0, len(array) - i - 1):
            
            if array[j] > array[j + 1]:
                (array[j], array[j + 1]) = (array[j + 1], array[j])
                swapped = False

                if swapped:
                    break

# this function gives the feedback of the overall season

def feedback(total_pt): 
    if total_pt >= 60:
        print("Good season")
    elif total_pt >= 45:
        print("Tough season")
    else:
        print("Bad season")

teams = int(input("Enter the number of teams = "))

all_teams = []  # this is an empty list

for i in range(0, teams):
    team_name = str(input("Enter the name of team = "))
    print(team_name)

    match_play = int(input("Enter number of matches played = "))
    print(match_play)

    win = int(input("Enter the number of matches won by team = "))
    print(win)
    
    draw = int(input("Enter the number of matches draw by team = "))
    print(draw)
    
    loss = int(input("Enter the number of matches lose by team = "))
    print(loss)

    total = win + draw + loss
    print(str(total) + " matches played")

    win = win * 3
    draw = draw * 1
    loss = loss * 0

    total_pt = win + draw + loss
    print(str(total_pt) + " points in " + str(total) + " matches")

    feedback(total_pt) #function called
    
total_pt = []
bubble_sort(total_pt)



