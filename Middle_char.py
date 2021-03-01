""" list = [1,2,3,4,5,6]

first_element = int(len(list)/2) - 1
second_element = int(len(list)/2)

print(list[first_element])
print(list[second_element]) """

# Question 1: Given a string of odd length greater 7, return a string made of the middle three chars of a given String
def getMiddleElement(sampleStr):
    middleIndex = int(len(sampleStr)/2)
    print('Original String is : ', sampleStr)
    middleThree = sampleStr[middleIndex-1:middleIndex+2]
    print('three middle elements are as follows : ', middleThree)

getMiddleElement("JohnDipPeta")
getMiddleElement("TollPipGate")

# Question 2: Given 2 strings, s1 and s2, create a new string by appending s2 in the middle of s1
def appendMiddle(s1,s2):
    middleIndex = int(len(s1)/2)
    print('Original Index are : ', s1, s2)
    middleString = s1[:middleIndex:] + s2 + s1[middleIndex:]
    print('After appending new string in middle : ', middleString)

appendMiddle("Ault", "Kelly")

def mix_string(s1, s2):
    first_char = s1[:1] + s2[:1]
    middle_char = s1[int(len(s1)/2):int(len(s1)/2) + 1] + s2[int(len(s2)/2):int(len(s2)/2) + 1]
    last_char = s1[len(s1) - 1] + s2[len(s2) - 1]
    res = first_char + middle_char + last_char
    print('Mix String is : ', res)

s1 = "America"
s2 = "Japan"
mix_string(s1,s2)

# program to calculate the length of string
def string_length(str1):
    count = 0
    for char in str1:
        count += 1
    return count
print(string_length('Atharva Hiwase'))

# program to calculate the frequency of characters in a string
def char_frequency(str1):
    dict = {}
    for n in str1:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    return dict
print(char_frequency('googel.com'))

# program to concatenate first and last 2 letter of a given string
def string_both_ends(str1):
    if len(str1) < 2:
        return ''

    return str1[0:2] + str1[-2:]

print(string_both_ends('AtharvaHiwase'))
print(string_both_ends('At'))
print(string_both_ends('A'))

# Get a string from a given string where all occurrences of
# its first char have been changed to '$',
# except the first char itself
def change_char(str1):
    char = str1[0]
    str1 = str1.replace(char, '$')
    str1 = char + str1[1:]

    return str1

print(change_char('restart'))

# 
def chars_mix_up(a,b):
    new_a = b[:2] + a[2:]
    new_b = a[:2] + b[2:]

    return new_a + ' ' + new_b
print(chars_mix_up('abc','xyz'))

# add 'ing' to the end of the string. If the string already exist with 'ing' then replace it with 'ly', and if the wors is less than 3, then leave it as it is.
def add_string(str1):
    length = len(str1)

    if length > 2:
        if str1[-3:] == 'ing':
            str1 += 'ly'
        else: 
            str1 += 'ing'
    return str1

# driver code
print(add_string('ab'))
print(add_string('abs'))
print(add_string('string'))
