total_matches = int(input("Enter the number of matches played = "))
win = int(input("Enter the number of matches won by team = "))
draw = int(input("Enter the number of matches draw by team = "))
loss = int(input("Enter the number of matches lose by team = "))

total = win + draw + loss
print(str(total) + " matches played ")
  
win = win * 3
draw = draw * 1
loss = loss * 0
 
total_pt = win + draw + loss
print(str(total_pt) + " points in " + str(total) + " matches")

if total_pt >= 55:
    print("Season was great.....")
elif total_pt >= 35:
    print("rough season huh...")
else:
    print("You must be relegated or really down")

