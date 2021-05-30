import sys
read = lambda : sys.stdin.readline().strip()

n=int(read())

def dfs(world,cnt,x,y):
  world[x][y]=0
  dx=[1,-1,0,0]
  dy=[0,0,1,-1]
  for i in range(4):
    n_x = x+dx[i]
    n_y = y+dy[i]
    if n_x>=0 and n_x<n and n_y>=0 and n_y<n:
      if world[n_x][n_y]==1:
        cnt= dfs(world,cnt+1,n_x,n_y)
  return cnt

world=[list(map(int,list(read()))) for _ in range(n)]
num=[]
for i in range(n):
  for j in range(n):
    if world[i][j]==1:
      num.append(dfs(world,1,i,j))
num.sort()

print(len(num))
for i in num:
  print(i)