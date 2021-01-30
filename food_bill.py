def calc_bill_amount(quantity_food, distance_in_kms, food_type):
    vegiterian_food = 120
    non_vegiterian_food = 150
    bill_amount = 0

    if quantity_food >= 1 and distance_in_kms >= 1:
        if food_type == "V":

            vegSubTotal = vegiterian_food * quantity_food
            if distance_in_kms <= 5:
                bill_amount = vegSubTotal
            elif distance_in_kms >= 5 and distance_in_kms <= 8:
                distance_charge = distance_in_kms - 3
                distance_charge *= 3
                bill_amount = vegSubTotal + distance_charge
            else:
                distance_charge = distance_in_kms - 8
                distance_charge *= 8
                bill_amount = vegSubTotal + distance_charge + 9

        elif food_type == "N":

            nonVegSubTotal = non_vegiterian_food * quantity_food
            if distance_in_kms <= 5:
                bill_amount = nonVegSubTotal
            elif distance_in_kms >= 5 and distance_in_kms <= 8:
                distance_charge = distance_in_kms -3
                distance_charge *= 3
                bill_amount = nonVegSubTotal + distance_charge
            else:
                distance_charge = distance_in_kms - 8
                distance_charge *= 8
                bill_amount = nonVegSubTotal + distance_charge + 9
            
        else:
            bill_amount = -1
    else:
        bill_amount = -1

    return bill_amount

bill_amount = calc_bill_amount("V",1,1)
print(bill_amount)


