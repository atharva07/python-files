# list comprehension
h_letters = []
for letter in 'human':
    h_letters.append(letter)
print(h_letters)

h_letters = [letter for letter in 'human']
print(h_letters)

number_list = [x for x in range(20) if x % 2 == 0]
print(number_list)

num_list = [y for y in range(100) if y % 2 == 0 if y % 5 == 0]
print(num_list)

obj = ["Even" if x % 2 == 0 else "odd" for x in range(10)]
print(obj) 

# transpose of matrix
a = [1,4,2,41,24,35,55]
del a[5]
print(a)

