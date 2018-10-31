t = int(input())
def fact(n):
    a=1
    for j in range(n):
        a = a*(j+1)
    return(a)
for i in range(t):
    n = int(input())
    print(fact(n))
