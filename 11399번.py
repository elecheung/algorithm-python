n=int(input())
a=list(map(int,input().split())) #한번에 list를 선언하면서 값들을 집어넣음
a.sort()
print(a)
sum=0
b=0
for i in range(0,n):
    b+=a[i]
    sum+=b
    print(sum)
print('{}'.format(sum))