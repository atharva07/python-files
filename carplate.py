# list of car plates
car_plates = ['AE2343', 'DE4324', 'RG4356', 'HT5432', 'IK9870', 'SE6578']

# list of ODD days
odd_days = ['MO', 'WE', 'FR']
# list of even days
even_days = ['TU', 'TH', 'SA']
pass_list = []
today = input('Enter day of week = ')
for plate in car_plates:
    last_digit = int(plate[-1])
    if today in odd_days and last_digit % 2 != 0:
        pass_list.append(plate)
    elif today in even_days and last_digit % 2 == 0:
        pass_list.append(plate)
    elif today == 'SU':
        pass_list.append(plate)

print(*pass_list, sep='\n')