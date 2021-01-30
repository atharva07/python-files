# creating a dog class
class Dog():
    def __init__(self, name):
        # Initialize dog object
        self.name = name

    def sit(self):
        print(self.name + " is sitting ")
    
my_dog = Dog('peso')

my_dog.sit()
print(my_dog.name + " is a great dog")

# inheritance
class SAEDog(Dog):
    def __init__(self, name):
        sup