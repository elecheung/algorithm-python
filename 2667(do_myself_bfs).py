import sys
read = lambda : sys.stdin.readline().strip()

n=int(read())
dx=[1,-1,0,0]
dy=[0,0,1,-1]
def bfs(world,cnt,x,y):
  world[x][y]=0
  queue=[]
  queue.append((x,y))
  while len(queue)>0:
    x,y=queue.pop()
    for i in range(4):
      nx, ny =x+dx[i], y+dy[i]
      if nx>=0 and nx<n and ny>=0 and ny<n:
        if world[nx][ny]==1:
          cnt+=1
          world[nx][ny]=0
          queue.append((nx,ny))
  return cnt

world=[list(map(int,list(read()))) for _ in range(n)]
ans=[]
for i in range(n):
  for j in range(n):
    if world[i][j]==1:
      ans.append(bfs(world,1,i,j))

print(len(ans))
for i in sorted(ans):
  print(i)