#def add_num(x, y):
    #return x + y

#def sub_num(a, b):
    #return a - b

#def make_pizza(topping = "bacon"):
#    print("have a " + topping + " pizza!")

# make_pizza()
# make_pizza("pepperoni")


# def master_add(pizza):
#    print("have a " + pizza + " pizza!")


# order = str(input("Enter the pizza name = ")) 
# master_add(order)

# vegiterian = ['cheese','cheese-burst','paparoni','corn-tomato','mexican-spinach']
# if order is vegiterian: 
#    print("You have ordered veg-pizza")
#else:
#   print("You have ordered non-veg pizza")

#diff = sub_num(5,2)
#print(diff)

#sum = add_num(3,4)
#print(sum)

class Dog():
    def __init__(self, name):
        self.name = name

    def sit(self):
        print(self.name + " is sitting ")

my_dog = Dog("Peso")

print(my_dog.name + " is a great dog!")
my_dog.sit()

