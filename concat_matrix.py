# two matrix of size M and N

M = 2
N = 2

def mergeMatrix(A,B):
    C = [[0 for j in range(2*N)]
          for i in range(M)]

    # merge two matrices
    for i in range(M):
        for j in range(N):
            
            # to store the elements of matrix A
            C[i][j] = A[i][j]
            # to store the elements of matrix B
            C[i][j+N] = B[i][j]

    for i in range(M):
        for j in range(2 * N):
            print(C[i][j], end = ' ')
        
        print()

# Driver code
if __name__ == '__main__':
    A = [[1,2],[3,4]]
    B = [[5,6],[7,8]]

    mergeMatrix(A,B)