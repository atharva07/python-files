# we can add anything in list like boolean, number, string
friends = ["Rahul","Pritam","Atharva","kartik","jimmy"]
#How to access list
print(friends)
print(friends[0]) # give index number to access particular element from lists
print(friends[1:]) # returns the elements from ndex 1 and so on
print(friends[1:3]) # access the elements from 1 and before 3 i.e. 2

# Now placing an another element in another index 
friends[1] = "Pappu"
print(friends[1])

friends.append('nana')
print(friends)
print(friends[-1])
friends.sort()
print(friends)

name = str(input('enter the name = '))

if name in friends:
    print("yes, he is present")
else:
    print('he is not present')
    friends.append(name)
    print(friends)

print(friends)

if 'Atharva' in friends:
    friends.remove('Atharva')
    friends.append('Lalit')
    print(friends)
else:
    print("we are cool")