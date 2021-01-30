def mergeSort(arr):
    if len(arr) > 1:
        # finding the mid
        mid  = len(arr)//2

        # dividing the arrays elements
        L = arr[:mid]
        # into 2 halves
        R = arr[mid:]
        # sorting the first half
        mergeSort(L)
        # sorting the second half
        mergeSort(R)

        i = j = k = 0

        # copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1

            k += 1

        # checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1 

def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()

# driver code
if __name__ == '__main__':
    arr = [12,11,13,5,4,6,7]
    print('Given array is', end="\n")
    printList(arr)
    mergeSort(arr)
    print('sorted array is', end="\n")
    printList(arr)