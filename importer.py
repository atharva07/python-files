# different ways to import module 
import my_module as mm

courses = ['History','Math','Science','Algebra']

index = mm.find_index(courses, 'Math')
print(index)

# another method
from my_module import find_index

courses = ['Alex','Morgan','David','Luther']

bar_search = find_index(courses,'Morgan')
print(bar_search)

# another method
from my_module import find_index as fi 

courses = ['History','Math','Science','Algebra']

index = fi(courses,'Algebra')
print(index)

# to import everything
from my_module import *

courses = ['History','Math','Science','Algebra']

index = find_index(courses,'History')
print(index)
print(test)

from my_module import find_index, test
import sys

courses = ['History','Math','Science','Algebra']

index = find_index(courses,'History')
print(index)
print(test)

print(sys.path) # gives the path of module imported and the complete information of the path of the module

