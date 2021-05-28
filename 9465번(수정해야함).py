t=int(input())

def count():
  a=[]
  n=int(input())
  for _ in range(2):
    a.append(list(map(int,input().split())))
  for i in range(n):
    a[0][i+1]=max(a[1][i+1],a[0][i+2])
    a[1][i+1]=max(a[0][i+1],a[1][i+2])
  result=max(a[0][n],a[1][n])
  return print(result)

for _ in range(t):
  count()