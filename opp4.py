class Employee:

    num_of_emps = 0
    raise_amt = 1.04

    europe = ['Germany','France','Spain','Iceland','England']
    asia = ['India','china','Pakistan']

    def __init__(self,first,last,pay,nationality):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@gamil.com'
        self.pay = pay
        self.nationality = nationality

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first,self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    def know_class(self):
        if self.pay >= 5000 and self.pay <= 20000:
            print('You are in class-3 tier...')
            print('You are getting some extra cash')
            self.pay += 7000
        elif self.pay >= 21000 and self.pay <= 45000:
            print('great you belong to class-2 tier')
            print('you are getting 3000 bonus')
            self.pay += 3000
        else:
            print('you guys belong to class-1 tier')
            print('no bonus for you guys....sorry')
            print('You have to pay immigration tax')
            self.pay -= 2899
    
    def know_nation(self):
        
emp_1 = Employee('Corey','Schafer', 40000,'Germany')
emp_2 = Employee('Atharva','Hiwase', 64788,'India')
emp_3 = Employee('Gylfi','Sigurdsson',54000,'Iceland')

emp_list = [emp_1,emp_2,emp_3] # created a list of employees 

print(Employee.raise_amt)
print(emp_1.raise_amt)
print(emp_2.raise_amt)
for Employee in (emp_list):
    Employee.know_class()
    print(f'The salary is as follows = ${Employee.pay}')
    