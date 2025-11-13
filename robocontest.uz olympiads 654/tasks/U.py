a,b=map(int,input().split())
a1,b1=map(int,input().split())
a2,b2=map(int,input().split())
a3,b3=map(int,input().split())
s=a+a1+a2+a3
s1=b+b1+b2+b3
if s>s1:
    print(1)
elif s<s1:
    print(2)
else:
    print(0)