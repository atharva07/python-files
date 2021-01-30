def change_name(mylist):
    mylist.append(5)
    print('values inside a function',mylist)
    return

def make_name(mylist1):
    mylist1.append(4)
    print('values inside a function',mylist1)
    return

mylist1 = [56,67,34]
make_name(mylist1)
print('values outside a function', mylist1)

mylist = [34,45,667]
change_name(mylist)
print('values outside a function',mylist)

def list_append(my_list):
    my_list.append(6)
    return

my_list = [45,65,34,6]
list_append(my_list)
print(my_list)

main_list = [4,565,23,43,12,78]

condition = True
x = 1 if condition else 0
print(x)

array2 = [4,65,44,223,12,145,46]
print(sorted(array2))
