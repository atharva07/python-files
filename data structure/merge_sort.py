# this is an algorithm of merge sort. Merge sort is very popular algorithm and a great way to develop confidence in recursive
# programs. This algorithm uses divide and conquer strategy.
# Merge Sort Algorithm
# MergeSort(A,p,r):
#   if p>r
#       return
#   q = (p+r)/2
#   mergesort(A,p,q)
#   mergesort(A,q+1,r)
#   mergesort(a,p,q,r)

def MergeSort(array):
    if len(array) > 1:
        
        # r is a pointer where the array is divided into two sub-arrays
        r = len(array)//2
        L = array[r:]
        M = array[:r]

        # Sort the tow halves
        MergeSort(L)
        MergeSort(M)

        i = j = k = 0

        # until we reach the end of L or M, pick larger among L and M and place them in correct position at A[p..r]
        while i < len(L) and j < len(M):
            if L[i] < M[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = M[j]
                j += 1
            k += 1

        # when we run out of elements in either L or M, pick up the remaining elements up the remaining elements and put in A[p..r]
        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1

        while j < len(M):
            array[k] = M[j]
            j += 1
            k += 1
# print the array list
def printList(array):
    for i in range(len(array)):
        print(array[i], end=' ')
    print()

# driver program
if  __name__ == '__main__':
    array = [6,5,44,56,34,789,43,24,56]
    MergeSort(array)

    print('Sorted array is as follows = ')
    printList(array)