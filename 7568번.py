n=int(input())
x=[]
rank=[]
for _ in range(n):
  x.append(list(map(int,input().split())))
for i in range(n):
  grade=1
  for j in range(n):
    if(x[i][0] < x[j][0] and x[i][1] < x[j][1]):
      grade+=1
  rank.append(grade)
for i in rank:
  print(i,end=' ')