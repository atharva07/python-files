def removeDuplicates(arr, n):
    if n == 1 or n == 2:
        return n
    
    temp = list(range(n))

    j = 0
    for i in range(0,n-1):
        if arr[i] != arr[i+1]:
            temp[j] = arr[i]
            j += 1

    temp[j] = arr[n-1]
    j += 1

    for i in range(0,j):
        arr[i] = temp[i]

    return j

# driver code
arr = [1,2,2,2,4,5,5,6,6,7,8,8]
n = len(arr)

n = removeDuplicates(arr, n)

for i in range(n):
    print("%d"%(arr[i]), end=" ")
