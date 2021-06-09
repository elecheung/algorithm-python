import sys
from collections import deque

m,n=map(int,input().split())
box=[list(map(int,input().split())) for _ in range(n)]

q=deque()
p=deque()

def bfs(q,cnt):
  dx=[1,-1,0,0]
  dy=[0,0,1,-1]
  while q:
    cnt+=1
    for _ in range(len(q)):
      a,b=q.popleft()
      for k in range(4):
        nx, ny = a+dx[k], b+dy[k]
        if 0<= nx <n and 0<= ny < m and box[nx][ny]==0:
          box[nx][ny]=1
          q.append([nx,ny])
  for to in box:
    if 0 in to:
      return -1    
  return cnt-1

for i in range(n):
  for j in range(m):
    if box[i][j]==1:
      q.append([i,j])
count=bfs(q,0)      
  
print(count)