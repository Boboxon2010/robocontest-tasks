a,b,c=map(int,input().split())
kichik=min(a,b,c)
katta=max(a,b,c)
middle=a+b+c-kichik-katta
print(kichik,middle,katta)