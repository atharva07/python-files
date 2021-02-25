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
