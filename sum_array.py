# sum of an array
def _sum(arr,n):
    return(sum(arr))

arr = []
arr = [3,4,2,5,4]
n = len(arr)
ans = _sum(arr,n)
print('sum of an array is ', ans)

# find the largest element of an array
def largest(arr,n):
    max = arr[0]
    for i in range(1,n):
        if arr[i]>max:
            max = arr[i]
    return max

arr = [4,56,34,223,3422,3456,3214]
n = len(arr)
answer = largest(arr,n)
print('largest element of array is ', answer)
