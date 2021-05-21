n=int(input())
b=[]
sum=0
for i in range(0,n):
  a=int(input())
  b.append(a)
  if a==0:
    del b[-1]
    del b[-1]
for i in b:
  sum+=i
print(sum)