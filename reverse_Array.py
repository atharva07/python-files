def reverseArray(A, start, end):
    while start < end:
        A[start], A[end] = A[end], A[start]
        start += 1
        end -= 1

# driver code
A = [1,2,3,4,5,6]
print(A)
reverseArray(A,0,5)
print("Reversed list is")
print(A)

def largest(arr,n):
    max = arr[0]
    
    for i in range(1,n):
        if arr[i] >  max:
            max = arr[i]
    return max

# driver code
arr = [10,45,32,543,456,345,65]
n = len(arr)
Ans = largest(arr, n)
print(Ans)
