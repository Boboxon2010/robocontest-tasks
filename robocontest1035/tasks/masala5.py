n=input()
alifbo=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
s=0
l=0
for i in alifbo:
    k=n.count(i)
    
    if k>1 and k%2==1:
        s+=k-1
        l+=1
    elif k==1:
        l+=1
    elif k>1 and k%2==0:
        s+=k
    else:
        continue
if l>0:
    print(s+1)
else:
    print(s)