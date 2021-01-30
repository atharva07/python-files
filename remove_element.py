def deleteElement(arr,n,x):
    
    # search x in array
    for i in range(n):
        if (arr[i] == x):
            break
    
    # if found x
    if (i < n):
        n = n - 1
        for j in  range(i,n,1):
            arr[j] = arr[j+1]

    return n

if __name__ == '__main __':
    arr = [1,3,22,5,34,5]
    n = len(arr)
    x = 22

    n = deleteElement(arr,n,x)

    print('Modified array is')
    for i in range(n):
        print(arr[i], end = ' ')

