class Football:
    def __init__(self, name, age, team, goals):
        self.name = name
        self.age = age
        self.team = team
        self.goals = goals

players = 0 
players = int(input("Enter the number of players = "))
if players > 0:
    name = str(input("Enter the name of player = "))
    age = str(input("Enter his age = "))
    team = str(input("Enter the name of his team = "))
    goals = int(input("Enter the total goals scored last season = "))
    print("these are the players")
else:
    print("no players registered")

Football(name, age, team, goals)
print("This is a list")

