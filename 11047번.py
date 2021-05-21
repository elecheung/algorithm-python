n,k=map(int,input().split())
a=[]
count=0
for i in range(0,n):
    a.append(int(input()))

for i in range(n-1,-1,-1):
    b=k//a[i]
    if b==0:
        k=k
    elif k==0:
        break
    else:    
        k=k-a[i]*b
        count+=b
        #print('{}'.format(count))
print('{}'.format(count))
    #print('{}'.format(i))