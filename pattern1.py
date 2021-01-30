# 1
rows = 6
for num in range(rows):
    for i in range(num):
        print(num, end = " ")
    print("  ")

# 2
rows = 5
for row in range(1, rows + 1):
    for column in range(1, row + 1):
        print(column, end = " ")
    print(" ")

def greet(first_name, last_name):
    print(f'hello {first_name} {last_name}')
    print('how are you')

greet('John', 'smith')

a = 34
b = 22

# swapping 
a, b = b, a
print(a, b) 

# fibonacci number
def fibonacci(n):
    a = 0
    b = 1
    if n <= 0:
        print('incorrect number')
    elif n == 1:
        return b
    else:
        c = a + b
        a = b
        b = c
    return b

print(fibonacci(9))

# swapping first and last element
def swaplist(newlist):
    size = len(newlist)

    # swapping
    temp = newlist[0]
    newlist[0] = newlist[size - 1]
    newlist[size - 1] = temp

    return newlist

newlist = [24,32,25,46,57]
print(swaplist(newlist))

# swapping frist and last element  from string
def swap(string):
    start = string[0]
    end = string[-1]

    swapped_string = end + string[1:-1] + start
    print(swapped_string)

swap('python')

# matrix multiplication
x = [[12,3,5],
    [3,6,13],
    [29,14,17]]

y = [[15,26,24,27],
    [34,25,23,2],
    [16,28,33,9]]

result = [[0,0,0,0],
        [0,0,0,0],
        [0,0,0,0]]

for i in range(len(x)):
    for j in range(len(y[0])):
        for k in range(len(y)):
            result[i][j] += x[i][k] * y[k][j]

for r in result:
    print(r) 

# split array from front and place it at back 
def splitArr(arr,n,k):
    for i in range(0,k):
        x = arr[0]
        for j in range(0, n-1):
            arr[j] = arr[j+1]
        arr[n-1] = x

arr = [12,10,5,6,53,36]
n = len(arr)
position = 2
splitArr(arr,n,position)

for i in range(0,n):
    print(arr[i], end=' ')
   
# program to split string and join using different delimiter
def split_string(string):
    list_string = string.split(' ')
    return list_string

def join_string(list_string):
    string = '-'.join(list_string)
    return string

if __name__ == '__main__':
    string = 'geeks for geeks'

    list_string = split_string(string)
    print(list_string)

    new_string = join_string(list_string)
    print(new_string)

# matrix multiplication
# print('Enter n for nxn matrix')
# n = int(input())

# matrix1 = []
# matrix2 = []

# print('Enter elements of 1st matrix')
# for i in range(0,n):
#     print('Enter elements of',i,'column, seperated by space')
#     matrix1.append(int,input().split())
# print(matrix1)

# print('Enter the elements of 2nd matrix')
# for i in range(0,n):
#     print('enter elemets of',i,'column, seperated by space')
#     matrix2.append(int,input().split())
# print(matrix2)

# add_matrix = []
# for i in range(0,n):
#     a = []
#     for j in range(0,n):
#         a.append(matrix1[i][j] + matrix2[i][j])
#     add_matrix.append(a)
# print(add_matrix)

# fizzbuzz problem
class Solution(object):
    def fizzbuzz(self, n):
        result = []
        for i in range(1, n+1):
            if i%3 == 0 and i%5 == 0:
                result.append('fizzbuzz')
            elif i%3 == 0:
                result.append('fizz')
            elif i%5 == 0:
                result.append('buzz')
            else: 
                result.append(str(i))
        return result
obj1 = Solution()
num = int(input('enter the number = '))
print(obj1.fizzbuzz(num))

# code to check if 2 matrices are identical
def areSame(A,B):
    for i in range(n):
        for j in range(n):
            if (A[i][j] != B[i][j]):
                return 0
    return 1

A = []
n = int(input('Enter n for n*n matrix = '))
print('Enter the elements = ')
for i in range(n):
    row = []
    for j in range(n):
        row.append(int(input()))
    A.append(row)
print(A)

print('Display Array')
for i in range(n):
    for j in range(n):
        print(A[i][j], end=' ')
    print()

B = []
n = int(input('Enter n for n*n matrix = '))
print('Enter the elements = ')
for i in range(n):
    row = []
    for j in range(n):
        row.append(int(input()))
    B.append(row)
print(A)

print('Display Array')
for i in range(n):
    for j in range(n):
        print(B[i][j], end=' ')
    print()

if (areSame(A,B) == 1):
    print('matrices are identical')
else:
    print('matrices are not identical')