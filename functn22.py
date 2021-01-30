def area_of_tri(length, breadth):
    return length * breadth

def area_of_sq(side):
    return side * side 

lent = int(input("Enter the length of side = "))
bret = int(input("Enter the breadth of side = "))
side_sq = int(input("Enter the side for area = "))

if lent > 2 and bret > 2:
    area = area_of_tri(lent, bret)
    print("Area of triangle is", area)
else:
    print("your size is too small")


area_sq = area_of_sq(side_sq)
print("Area of square is", area_sq)

def table(n,i):
    print (n*i)
    i = i + 1
    if i<=10:
        table(n,i)

num = int(input("Enter the number of table you want = "))
table_num = table(num)
print(table_num)

