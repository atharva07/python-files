# function to find the pair in an array with a given sum using sorting 
def findPair(A, sum):
    # sort the list using ascending sort
    A.sort()

    # maintain the indices pointing to the endpoints of the list
    (low,high) = (0, len(A)-1)

    # loop till the search space is exhausted
    while low < high:
         
        if A[low] + A[high] == sum:
            print('pair found', (A[low],A[high]))
            return

        # increment 'low' index if the total is less than the desired sum
        # decrement 'high' index if the total is greater than the desired sum
        if A[low] + A[high] < sum:
            low = low + 1
        else:
            high = high - 1
    print('No pair found')

# driver code
if __name__ == '__main__':
    A = [8,7,2,5,3,1]
    sum = 10

    findPair(A,sum)        
