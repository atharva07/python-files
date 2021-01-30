# quicksort algorithm is based on a divide and conquer approach in which the array is split into sub-arrays and these 
# sub-arrays are recursively called to sort the elements. there are few things we have to do first.
# 1. The pivot element is chosen from the array. We can choose any element we want.
# 2. Elements smaller than the pivot elements are put on the left side and elements greater than the pivot element are put on the right side.

# quick sort algorithm
# quickSort(array, leftmostIndex, rightmostIndex)
#   if(leftmostIndex < rightmostIndex)
#       pivotIndex <- partition(array, leftmostIndex, rightmostIndex)
#       qucikSort(array, leftmostIndex, pivotIndex)
#       quickSort(array, pivotIndex + 1, rightmostIndex)
# partition(array, leftmostIndex,rightmostIndex)
#   set rightmostIndex as pivotIndex
#   storeIndex <- leftmostIndex - 1
#   for i <- leftmostIndex + 1 to rightmostIndex
#   if  element[i] < pivotElement
#       swap element[i] and element[storeIndex]
#       storeIndex++
#   swap pivotElement and element[storeIndex+1]
# return storeIndex + 1       

# function to partition the array on the basis of pivot element\
def partition(array, low, high):
    # Select the pivot element
    pivot = array[high]
    i = low - 1

    # put the elements smaller than pivot on the left side and the greater on the right side
    for j in range(low,high):
        if array[j] <= pivot:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])
    (array[i+1], array[high]) = (array[high], array[i+1])
    return i + 1

def quickSort(array,low,high):
    if low < high:
        # selecting pivot position and placing greater elements 
        pi = partition(array,low,high)
        # sort the elements on the left of pivot element
        quickSort(array,low,pi-1)
        # sort the elements on the right of pivot element
        quickSort(array,pi+1,high)

data = [45,65,3,49,23,39,12,32]
size = len(data)
quickSort(data,0,size-1)
print('sorted array is as follows')
print(data)