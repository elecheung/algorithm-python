n=int(input())
v=int(input())
matrix=list([0]*(n+1) for _ in range(n+1))
for _ in range(v):
  from_n,to_n=map(int,input().split())
  matrix[from_n][to_n] = matrix[to_n][from_n]=1
visit=list([0]*(n+1))

def bfs(first):
  count=0
  queue=[first]
  visit[first]=1
  while queue:
    first=queue.pop(0)
    for i in range(1,n+1):
      if visit[i]==0 and matrix[first][i]==1:
        count+=1
        queue.append(i)
        visit[i]=1
  return count

print(bfs(1))