# python code to count the frequency of string using naive method
test_str = "geeksforgeeks"

# intializing count to zero
count = 0
for i in test_str:
    if i == 'e':
        count = count + 1
print("the frequency is as follows = " + str(count))

# there is another method to count the freqency of the occurence of string using count() 
test_str1 = "geeksforgeeks"

counter = test_str1.count('e')
print('the frequency of string is as follows = ' + str(counter))

# method number 3 is as follows
# this method uses a library called as collections
# from collections we are importing counter() 
from collections import Counter

# intializing string
test_str2 = "geeksforgeeks"

count = Counter(test_str2)
print('The frequency of string is as follows = ' + str(count['e']))