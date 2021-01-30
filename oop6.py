class Carmodel:
    def __init__(self,brand,model,price,color,speed):
        self.brand = brand
        self.model = model
        self.price = price
        self.color = color
        self.speed = speed
    
    Carmodel.num_of_cars = 1

    def car_name(self):
        return '{} {}'.format(self.brand,self.model)

    def know_speed(self):
        if self.speed >= 95:
            print('You got $56 ticket')
            self.price += 56
            print(self.price)
        else:
            print('safe to go.....') 