
def f(x):
    s=0
    
    for k in range(n+1):
        s+=1+3*k+3*k*k
        
    return s
n=int(input())
print((f(n))%(pow(10,9)+7))