import re
from re import split

print(split('\W', 'Words, words, words'))
print(split('\W+', "Words, words, Words"))

print(re.split('[a-e]+', 'Aey, Boy oh boy, come here', flags=re.IGNORECASE))

# subString 
print(re.sub('ub', '~*', 'Subject has Uber booked already', flags=re.IGNORECASE))

print(re.sub('ub', '~*', 'Subject has booked Uber Already'))

print(re.sub('ub', '~*', 'Subject has booked Uber Already', count=1, flags=re.IGNORECASE))

print(re.sub(r'\sAND\s', ' & ', 'Baked Beans and Spam', flags=re.IGNORECASE))

# subn() function
print(re.subn('ub', '~*', 'Subject has Uber booked Already'))
t = re.subn('ub', '~*', 'Subject has booked Uber already', flags=re.IGNORECASE)

print(t)
print(len(t))
