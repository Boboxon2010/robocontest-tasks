a=int(input())
bir_bir=a//100000
bir_ikki=(a//10000)%10
bir_uch=(a//1000)%10
ikki_bir=(a//100)%10
ikki_ikki=(a//10)%10
ikki_uch=a%10
s1=bir_bir+bir_ikki+bir_uch
s2=ikki_bir+ikki_ikki+ikki_uch
if s1==s2:
    print('Yes')
else:
    print('No')