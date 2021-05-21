n= int(input())
i=1
c=0
sum=0
while(1):
    c=n-sum
    sum=int(i*(i+1)//2)
    i+=1
    if sum>=n:
        i-=1
        break
a=int(i-c+1)
b=int(c)
if i%2==1:
    print('{}/{}'.format(a,b))
else:
    print('{}/{}'.format(b,a))