n=int(input())
a=[]
for _ in range(n):
  a.append(list(map(int,input().split())))
for i in range(n-1,-1,-1):
  for j in range(0,i):
    a[i-1][j]+=max(a[i][j],a[i][j+1])
print(a[0][0])