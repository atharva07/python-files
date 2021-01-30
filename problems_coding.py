# 1. vowel or consonant 
def vowel_or_consonant(ch):
    if (ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u' or ch == 'A' or ch == 'E' or ch == 'I' or ch == 'O' or ch == 'U'):
        print('Vowel')
    else:
        print("consonant")

ch = input("Enter the Chracter = ")
vowel_or_consonant(ch)

# 2. check if an alphabet is character is alphabet or not
cha = input("Enter the charcter = ")
if ((cha >= 'a' and cha <= 'z') or (cha >= 'A' and cha <= 'Z')):
    print(cha, end="")
    print("It is a character")
else:
    print(cha, end="")
    print("It is not a character")

# 3. positive or negative number
num = int(input('Enter number = '))
if (num > 0):
    print('positive')
else:
    print('negative')

# 4. Area of circle
from math import pi
def area_of_circle(radius):
    return str(pi * radius ** 2)
radius = int(input('Enter radius = '))
print('The area of circle is ' + area_of_circle(radius))

# 5. prime numbers in a given range
