hh,mm=map(int,input().split(':'))
t=int(input())
m=mm+t
if t>=60:
    hh+=t//60
    mm=t%60
elif m>=60:
    hh+=1
    mm=m-60
if hh>=24:
    hh=0
print(f"{hh:.2f}",':',f"{mm:.2f}")
