# sorting of lists......
li = [6,8,5,3,1,2,4,7,9] 
# sorting by creating a new variable
s_li = sorted(li)
print('sorted version = \t',s_li)
print('original version = \t',li)
# sorting without creating a new variable
li.sort()
print('sorted version = \t',li)

s_li = sorted(li, reverse=True) # sorts list in descending order
print('original version = \t',li)
print('sorted version = \t',s_li)

# we can also do this
li.sort(reverse=True)
print('sorted version = \t',li)

# sorting of tuples......
tup = (4,8,9,1,3,2,5,7,6)
s_tup = sorted(tup)
print('tuple\t',s_tup)

# sorting of dictionary.....
di = {'name': 'Corey', 'job': 'programmer', 'age': None, 'os': 'Windows'}
s_di = sorted(di)
print('dict\t',s_di)

# sorting based on some criteria
li = [-6,-5,-4,1,2,3]
c_li = sorted(li, key=abs) # abs value function
print(c_li)

class Employee():
    def __init__(self,name,age,salary):
        self.name = name
        self.age = age
        self.salary = salary
    def __repr__(self):
        return '({},{},${})'.format(self.name,self.age,self.salary)

from operator import attrgetter # sorting using some libraries

e1 = Employee('Carl',34,15000)
e2 = Employee('David',37,23000)
e3 = Employee('Duke',25,7000)
e4 = Employee('Aaron',54,33000)

employees = [e1,e2,e3,e4]

# making a custom function
def e_sort(emp):
    return emp.age

s_employees = sorted(employees, key=e_sort, reverse=True)
print(s_employees)
s_employees = sorted(employees, key=lambda e: e.name)
print(s_employees)
s_employees = sorted(employees, key=attrgetter('salary'), reverse=True)
print(s_employees)

li_2 = [45,34,52,22,21,38,23,29]
v_li_2 = sorted(li_2, reverse=True)
print(v_li_2)

class Freshers():
    def __init__(self,name1,age1,pay):
        self.name1 = name1
        self.age1 = age1 
        self.pay = pay

    def __repr__(self):
        return '({},{},${})'.format(self.name1,self.age1,self.pay)

from operator import attrgetter

f1 = Freshers('nitin',23,24000)
f2 = Freshers('mitin',22,21000)
f3 = Freshers('jatin',24,27000)

freshers2020 = [f1,f2,f3]

def fr_sort(fre):
    return fre.age1

f_fresher = sorted()