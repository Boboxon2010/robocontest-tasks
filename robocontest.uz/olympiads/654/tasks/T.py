a,b,c,d=map(int,input().split())
eng_katta=max(a,b)
eng_katta1=max(c,d)
eng_kichik=min(a,b)
eng_kichik1=min(c,d)
s=eng_kichik*eng_kichik1+eng_katta*eng_katta1
print(s)