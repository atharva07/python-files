# initializng list 
test_list = [3,5,6,2,34,43,54]
print("checking if 5 is present or not (using loop) : ")

# checking if 5 exist or not
for i in test_list:
    if(i == 5):
        print("element exist")

if (5 in test_list):
    print('yes')
else:
    print('no')

from bisect import bisect_left

test_set_list = [1,3,6,5,3,4]
test_set_bisect = [1,3,6,5,3,4]

print('checking if 4 is present or not (using set)')
test_set_list = set(test_set_list)
if 4 in test_set_list:
    print('yes')

# checking using sort 
test_set_bisect.sort()
if bisect_left(test_set_bisect, 4):
    print('yes')
