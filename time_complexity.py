# O(1) Constant 
def func1(N):
    return(N[0]+N[1])

func1([1,2,3,4,5,6])

# O(N) linear
def func2(N):
    for i in N:
        print(i)

func2([1,2,3,4,5])

# O(N^2) quadtratic 
def func3(N):
    for i in range(len(N)):
        for j in range(len(N)):
            print(N[i],N[j])
        
func3([1,2,3,4,5,6])

# Logarithmic
x = len([1,2,3,4,5,6,7,8])
while x>0:
    y = 2+2
    x = x // 2
    print(y)
    print(x)

