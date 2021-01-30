# program to search an element row-wise and column-wise
def search(mat,n,x):
    i = 0
    j = n - 1
    while(i < n and j >= 0):
        if (mat[i][j] == x):
            print('found element at', i , '', j)
            return 1
            if (mat[i][j] > x):
                j -= 1
            else:
                i += 1

    print('element not found')
    return 0

# driver code
mat = [[34,5,23,21,43],
       [45,76,22,1,20],
       [12,23,41,88,65],
       [67,42,33,40,91]]
search(mat,4,42)

