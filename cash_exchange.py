amount_dollars = int(input("Enter the amount in dollars = "))
rate = 78.5
amount_rupees = amount_dollars * rate
print('total amount in rupees = ',amount_rupees)

list_dollars = []

if amount_rupees >= 20000:
    amount_rupees += 5000
    print(amount_rupees)
    if amount_rupees is not list_dollars:
        list_dollars.append(amount_rupees)
        print(list_dollars)
    else:
        print(list_dollars)
else:
    amount_rupees -= 2340
    print(amount_rupees)

def days(i):
    switcher = {
        0: 'sunday',
        1: 'monday',
        2: 'tuesday',
        3: 'wednesday',
        4: 'thursday',
        5: 'friday',
        6: 'saturday'
    }
    return switcher.get(i, "Invalid key")

print(days(4))

if switcher == 0:
    rate = 87.16
    inr_amount = rate * amount_currency
    print(inr_amount)
elif switcher == 1:
    rate = 70
    inr_amount = rate * amount_currency
else:
    print("Invalid Input")

def currency(i):
    switcher = {
        0: 'EURO',
        1: 'DOLLLAR',
        2: 'POUND',
        3: 'PESO',
        4: 'YEN',
        5: 'AUS DOLLAR'
    }
    return switcher.get(i, "Invalid input")

amount_currency = int(input("Enter the amount = "))
print(currency(1)