n=int(input())
i=1
sum=0
if n==1:
    i=i
else:
    while(1):
        sum=3*i*(i+1)+1
        i+=1
        if sum >= n:
            break
print(i)