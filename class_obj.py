# definition of class 
class Person:
    # initializing the variables
    name = ""
    age = 0

    # defining constructor
    def __init__(self, personName, personAge):
        self.name = personAge
        self.age = personAge

    # defining class methods
    def showName(self):
        print(self.name)

    def showAge(self):
        print(self.age)
    
    # end of class definition

# creating an object of class
person1 = Person("john",45)
person2 = Person("david",35)
# calling the memeber methods of the objects
person1.showAge()
person2.showAge()