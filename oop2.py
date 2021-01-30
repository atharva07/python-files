# the object is the instance of a class
# object is mutable if it can be altered dynamically
# The process of creating an object can be called instantiation.
# 'self' is an instance of an class
#class Employee:
    #def __init__(self, first, last, pay): # in barcket arguments are passed
        #self.first = first ---------the self is used as a reference variable---------
        #self.last = last
        #self.pay = pay
        #self.email = first + '.' + last + '@company.com'
    
    #def fullname(self):
        #return '{} {}'.format(self.first,self.last)

# this are instance variable
#emp_1 = Employee('James','rodriguez',50000) 
#emp_2 = Employee('Test','User',60000)

#print(emp_1) # this is calling of instance variables
#print(emp_2)

# this are attributes of class
# this is a manual method
#emp_1.first = 'James'
#emp_1.last = 'Rodriguez'
#emp_1.email = 'JamesRogrigues234@gamil.com'
#emp_1.pay = 60000

#emp_2.first = 'Test'
#emp_2.last = 'User'
#emp_2.email = 'TestUser123@gamil.com'
#emp_2.pay = 60000

#print(emp_1.email)
#print(emp_2.pay)

#print('{} {}'.format(emp_2.first,emp_2.last))
#print(emp_2.fullname())
# first, last, pay are the attributes of the class Worker
class Worker:
    raise_amount = 1.04

    def __init__(self,first,last,pay):
        self.first = first # these are instance attributes
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@gamil.com'
    
    def Fullname(self):
        return '{} {}'.format(self.first,self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

wor_1 = Worker('atharva','hiwase',50000)
wor_2 = Worker('bunny','patel',45000)
#wor_1 = Worker()
#wor_2 = Worker()
#print(wor_1)
#print(wor_2)

#wor_1.first = "Atharva"
#wor_1.last = "Hiwase"
#wor_1.email = "Atharva@gamiol.com"

# print(wor_1.email)
print(wor_2.pay)  # pay before applying raise
wor_2.apply_raise()
print(wor_2.pay) # pay after applying raise
# print(wor_2.Fullname())

# calling with the use of class i.e. print(Class.method(instance))
# print(Worker.Fullname(wor_1))

#print(wor_1.raise_amount)
#print(Worker.raise_amount)

# print(Worker.__dict__)

# instance attribute has a specific value to a particular instance of a class.
# class attribute has the same value for all the class instance.

class Dog:
    #class attribute
    species = "Labrador"

    def __init__(self,name,age):
        self.name = name # these are instance attribute
        self.age = age

buddy = Dog("Buddy",7)
miles = Dog("Miles",5)

print(buddy.species)
cool = buddy.name
print(cool)
umar = miles.age
print(umar)
print(miles.age)

buddy.age = 6 # values of the intstance attributes can be changed those are not permanent
print(buddy.age)

print(miles.species)

species = "Rot-villar"
print(species)

miles.species = "Dobarman"
print(miles.species)

class Lion:
    Type_of_lion = "African-American"
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    # Instance method
    def description(self):
        return f"{self.name} is {self.age} years old"

    # Another Instance method
    def speak(self,sound):
        return f"{self.name} makes {sound} noice"

kevin = Lion("Kevin",13)
print(kevin.description())

print(kevin)

kevin.speak("Roar")
print()

start = 11
end = 34

#for i in range(start,end):
    #if i > 1:
        #for j in range(2,i):
            #if (i % j==0):
                #break
            #else:
                #print(i)

squares = []
for x in range(0,10):
    squares.append(x**2)
print(squares)

if 5 in squares:
    print('the elemeent is present')
else:
    print('the element is not present')
    squares.append(5) 
    print(squares)




