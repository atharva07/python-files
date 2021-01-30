def fullname(first_name,last_name):
    compl_name = first_name + last_name
    return compl_name

f_name = input("Enter the first name = ")
l_name = input("Enter the last name = ")
name_output = fullname(f_name,l_name)
print(name_output)

pl_list = []
maxLength = 4
while len(pl_list) >= maxLength:
    player = input("Enter your fav player = ")
    pl_list.append(player)  
    print(pl_list)
print('This is your player list ')
print(pl_list)

class MasterChef:

    def __init__(self,house,)
