alifbo=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
ALIFBO=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
k=int(input())
matn=input()
natija=''
for i in matn:
    if i in alifbo:
        index=alifbo.index(i)
        natija+=alifbo[(index+k)%26]
    elif i in ALIFBO:
        index=ALIFBO.index(i)
        natija+=ALIFBO[(index+k)%26]
    else:
        natija+='_'
print(natija)   