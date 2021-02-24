# here are we are using abs() function whcih returns 
# absolute value of given argument, that is between given argument and 
# zero. 
""" from string import ascii_lowercase

def get_freq(test_str):

    freqs = {char: 0 for char in ascii_lowercase}

    # counting frequency
    for char in test_str:
        freqs[char] += 1
    return freqs

test_str1 = 'aaccbba'
test_str2 = 'aaccbbc'

print('The orignal string 1 is : ' + str(test_str1))
print('The original string 2 is : ' + str(test_str2))

# initializing k
K = 2

# getting Frequencies
freqs_1 = get_freq(test_str1)
freqs_2 = get_freq(test_str2)

# checking for frequencies 
res = True
for char in ascii_lowercase:
    if abs(freqs_1[char] - freqs_2[char]) > K:
        res = False
        break

print("Are strings similar : " + str(res)) """
                  
Str1 = "Atharva Inc."
Str2 = "Atharva Inc."

Result = Str1 == Str2
print(Result)