class Employee:

    raise_amt = 1.04

    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@gamil.com'
        self.pay = pay
    
    def fullname(self):
        return '{} {}'.format(self.first,self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay + self.raise_amt)

# the method of inheritence

class Developer(Employee): 
    raise_amt = 1.6

    def __init__(self,first,last,pay,prog_lang):
        super().__init__(first,last,pay)
        self.prog_lang = prog_lang

class Manager(Employee):

    def __init__(self,first,last,pay,employees=None):
        super().__init__(first,last,pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
    
    def add_emp(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)
    
    def remove_emp(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)
    
    def print_emp(self):
        for emp in self.employees:
            print('--->',emp.fullname())
        
class Director(Employee):

    def __init__(self,first,last,pay,manager=None):
        super().__init__(first,last,pay)
        if manager is None:
            self.manager = []
        else:
            self.manager = manager

    def add_mgr(self,mgr):
        if mgr not in self.manager:
            self.manager.append(mgr)

    def remove_mgr(self,mgr):
        if mgr in self.manager:
            self.manager.remove(mgr)

    def print_mgr(self):
        for mgr in self.manager:
            print('----->',mgr.fullname())     

    def __repr__(self):
        return "Employee('{}','{}','{}')".format(self.first,self.last,self.pay)
    
    def __str__(self):
        return "{} {}".format(self.fullname(),self.email)

    def __add__(self,other):
        return self.pay + other.pay


dev_1 = Developer('Atharva','hiwase',60000,'Python')
dev_2 = Developer('pawan','kumar',45000,'Java')

mgr_1 = Manager('David','Koffield',87000,[dev_1]) # [dev_1] states  that the manager supervises the dev 1
mgr_2 = Manager('Frances','Dcosta',78000,[dev_2])

dir_1 = Director('martin','guptill',145000,[mgr_1,mgr_2])

#print(mgr_1.email)

#mgr_1.print_emp()
#mgr_1.add_emp(dev_1)
#mgr_1.remove_emp(dev_1)
#mgr_1.add_emp(dev_2)
#mgr_1.print_emp()

#mgr_1.print_emp()
#dir_1.print_mgr()
#print(dev_1.pay)
#dev_1.apply_raise()
#print(dev_1.pay)
#print(dev_1.prog_lang)

#print(help(Developer))

#repr(mgr_1)
#str(mgr_2)

#print(dev_1.__repr__())
#print(dev_2.__str__())

#print(1+3)
print(int.__add__(4,5))
print(str.__add__('hello','world'))
print(int.__mul__(4,5))

print(mgr_1 + mgr_2)



