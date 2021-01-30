def high_class(total_salary):
    if total_salary >= 500000:
        print("he lives a better life")

def taxes(annual_pay, income_tax):
    if total_salary >= 450000:
        total_salary = annual_pay - income_tax
        print(total_salary)
    else:
        print("No deduction of taxes")

salary = int(input("Enter the salary of employee = "))
ann_pay = int(input("Enter the annual pay  to govt = "))
inc_tax = int(input("Enter the income tax  = "))
high_class(salary)
taxes(ann_pay, inc_tax)
        
