import sys
from collections import deque

def bsf(dep_x,dep_y,q):
  dx=[1,2,1,2,-1,-2,-1,-2]
  dy=[2,1,-2,-1,2,1,-2,-1]
  #a=start_x
  #b=start_y
  while q:
    a,b=q.popleft()
    for k in range(8):
      nx,ny=a+dx[k],b+dy[k]
      if 0<= nx < n and 0<= ny <n and chess[nx][ny]==0:
        chess[nx][ny]=chess[a][b]+1
        q.append([nx,ny])
  return chess[dep_x][dep_y]

t=int(input())
for _ in range(t):
  n=int(input())
  chess=list([0]*n for _ in range(n))
  start_x,start_y=map(int,input().split())
  dep_x,dep_y=map(int,input().split())
  q=deque()
  q.append([start_x,start_y])
  if start_x ==dep_x and start_y==dep_y:
    print(0)
  else:
    print(bsf(dep_x,dep_y,q))



