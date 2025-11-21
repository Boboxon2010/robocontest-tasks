n=int(input())
s=list(map(int,input().split()))
max=max(s)
qiyin_masalalar=max/2
a=0
for i in s:
    if i<qiyin_masalalar:
        a+=1
print(a)