a=int(input())
bir=a%1000
on=a%100//10
yuz=a//10%10
ming=a//1000
if bir%2==0 and on%2==0 and yuz%2==0 and ming%2==0:
    print('yes')
else:
    print('no')