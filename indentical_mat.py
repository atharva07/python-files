# check if two matrices are identical
N = 4
def areSame(A,B):
    for i in range(N):
        for j in range(N):
            if (A[i][j] != B[i][j]):
                return 0
    return 1

# driver code
A = [[1,2,3,4],
     [4,5,6,7],
     [8,9,10,11],
     [4,5,3,2]]

B = [[1,2,3,4],
     [4,5,6,7],
     [8,9,10,11],
     [4,5,3,2]]

if (areSame(A,B)==1):
    print('two matrices are identical')
else:
    print('matrices are not identical')