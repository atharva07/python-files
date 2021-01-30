# the bubble sort algorithm is given below. Bubble sort algorithm is one of the sorting algorithms.
# the pseudo code is given below
# bubbleSort(array)
#   for i <- 1 to indexoflastUnsortedElement - 1
#       if leftElement > RightElement
#           Swap leftElement and RightElement
#   end BubbleSort
# The code is given below

def BubbleSort(array):
    # loop runs two times, one for walking through the array 
    # another for the comparisons
    for i in range(len(array)):
        for j in range(0, len(array) - i - 1):
            if array[j] > array[j+1]:
                (array[j],array[j+1]) = (array[j+1], array[j])

data = [4,33,6,5,78,23,34]
BubbleSort(data)
print('Elements after sorting : ')
print(data)  