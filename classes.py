class Car:
    def __init__(self,color,mileage):
        self.color = color
        self.mileage = mileage

car_1 = Car(color= "Red", mileage = 34)
car_2 = Car(color= "Blue", mileage = 23)

for Car in (car_1,car_2):
    print(f"The car is {Car.color} and the mileage is {Car.mileage}")

toyota = car_1.color
print(toyota)  

Suzuki = car_2.mileage
print(Suzuki)
print(car_2.color)
print(car_1.mileage)

class bike:
    def __init__(self,model,mileage,price):
        self.model = model
        self.mileage = mileage 
        self.price = price
bike_1 = bike(model='AZ342DC', mileage=23, price=13000)
bike_2 = bike(model='DC548FE', mileage=21, price=15433)

for bike in (bike_1,bike_2):
    print(f"The number is {bike.model} and the mileage is {bike.mileage}")

if (bike.mileage >= 18):
    print('bike has good mileage')
else:
    print('no good')

print(bike_1.model)
print(bike_2.mileage)

mason = {"name": "Atharva",
        "Assignment": [34,41,33],
        "Test": [15,11,12],
        "lab": [34,41]}

print(mason['name'])
if (mason['name'] == 'Atharva'):
    print("Authorized, access granted")
else:
    print('No access, give correct ccredentials')

class Dog:
    attr1 = "mammal"
    attr2 = "dog"

    def fun(self):
        print('I am a', self.attr1)
        print('I am a', self.attr2)

Rodger = Dog()

print(Rodger.attr1)
Rodger.fun()