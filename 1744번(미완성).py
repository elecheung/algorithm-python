n=int(input()) 
a=[]
b=[]
for i in range(n):
    a.append(int(input()))
a.sort(reverse=True)
c=a.index(1)
d=a.index(0)
if len(range(c)%2==1): 
    for i in range(0,c-1,2):
        b.append(a[i]*a[i+1])
    b.append(c)
else:
    for i in range(0,c,2):
        b.append(a[i]*a[i+1])
for i in len(range(c,d)):
    b.append(1)
#마이너스부터 생각해야함!
a.sort(reverse=True)
e=a.index(0)
if len(range(e)%2==1):
     for i in range(0,e-1,2):
        b.append(a[i]*a[i+1])
     b.append(c)
else:
    for i in range(0,c,2):
        b.append(a[i]*a[i+1])
sum=0
for i in b:
    sum+=i
print(sum)