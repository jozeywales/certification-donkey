def fibLooping(n):
    a,b = 1,1
    for i in range(n-1):
        a,b = b,a+b
    return a

def fibRecursive(n):
    if n==1 or n==2:
        return 1
    return fibRecursive(n-1)+fibRecursive(n-2)