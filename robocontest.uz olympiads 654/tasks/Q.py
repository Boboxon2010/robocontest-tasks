#o'sish tartibi
a,b,c=map(int,input().split())
max=max(a,b,c)
min=min(a,b,c)
mid=a+b+c-max-min
print(min,mid,max)