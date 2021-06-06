n=int(input())
v=int(input())
matrix=[[0]*(n+1) for _ in range(n+1)]
visit=[0]*(n+1)
 
for _ in range(v):
  a,b=map(int,input().split())
  matrix[a][b]=matrix[b][a]=1

def dfs(first,count):
  visit[first]=1 
  for i in range(1,n+1):
    if visit[i]==0 and matrix[first][i]==1:
      visit[i]=1
      count = dfs(i,count+1)
  return count


print(dfs(1,0))