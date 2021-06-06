n,m=map(int,input().split())
map=[list(map(int,input())) for _ in range(n)]
visit=[[0]*m for _ in range(n)]
dx=[1,-1,0,0]
dy=[0,0,1,-1]

def bfs(x,y):
  queue = [[x,y]]
  visit[x][y]=1
  while len(queue)>0:
    x = queue[0][0]
    y = queue[0][1]
    queue.pop(0)
    for k in range(4):
      nx, ny = x+dx[k], y+dy[k]
      if 0 <= nx < n and 0<= ny <m:
        if map[nx][ny]==1 and visit[nx][ny]==0:
          queue.append([nx,ny])
          visit[nx][ny]=visit[x][y]+1
  return visit[n-1][m-1]
print(bfs(0,0))