name = str(input("Enter the name = "))
model = str(input("Enter the model name = "))
cahsis = int(input("Enter the cahsis number = "))

name_list  = ['bmw','mercedes','volkes wagon','audi','mclaren','porche']

prices = {
    'name': 'bmw','price':45000, 'porche': 56000, 'volkes wagon': 33000, 'audi': 48000, 'mclaren': 65000, 'mercedes': 40000
}

if name in name_list:
    print("we have that model")
    car_piece = int(input("How many models do you want = "))
    if car_piece <= 1 and car_piece >= 5:
        print("The amount you are asking for is avaliable") 
        if prices
else:
    print("we dont have that model")



