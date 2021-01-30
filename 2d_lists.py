number_grid1 = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]
print(number_grid1[0][0])

for row in number_grid1:
    for col in row:
        print(col)

number_grid2 = [
    [4,5,6],
    [7,6,3],
    [3,4],
    [9,8,7]
]
print(number_grid2[0][0])

for row in number_grid2:
    for col in row:
        print(col)

# tower of hanoi
def TowerOfHanoi(n, source, destination, auxiliary):
    if n == 1:
        print('move disk 1 from source', source, 'to destination', destination)
        return
    TowerOfHanoi(n-1, source, auxiliary, destination)
    print('move disk', n, 'from source', source, 'to destination', destination)
    TowerOfHanoi(n-1, auxiliary, destination, source)

n = 4
TowerOfHanoi(n, 'A', 'B', 'C')
