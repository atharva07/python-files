def binarySearch(array,x,low,high):
    while(low<=high):
        mid = low + (high-low)//2
        if array[mid] == x:
            return mid
        elif array[mid] < x:
            low = mid + 1
        else:
            high = mid - 1 
    return -1

array = [3,4,2,5,34,23,36]
x = 5
result = binarySearch(array,x,0,len(array))
if result != -1:
    print('Element is present at',str(result))
else:
    print('Element is not present')

# leap year program
def is_leap(year):
    leap = False
    if(year % 400 == 0):
        leap = True
    elif(year % 4 == 0 and year != 100):
        leap = True
    return leap

year = int(input('Enter the year = '))
print(is_leap(year))

# list comprehension 
results = []
for x in [1,2,3]:
    for y in [4,5,6]:
        results.append([x,y])
print(results)

# the list comprehension form is as follows
print([x,y] for x in [1,2,3] for y in [4,5,6]) 

# problem for nested list
n = int(input())
res = []
grade = []
for i in range(n):
    name = input()
    marks = float(input())
    res.append([name,marks])
    grade.append(marks)
print(res)
print(grade)
grade = sorted(set(grade))
print(grade)
m = grade[1]
print(m)
name = []
for val in res:
    if m == val[1]:
        name.append(val[0])
print(name) # unsorted name
name.sort()
print(name)
for nm in name:
    print(nm)
