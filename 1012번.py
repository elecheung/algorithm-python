import sys
from collections import deque

def bsf(x,y,q):
  dx=[1,-1,0,0]
  dy=[0,0,1,-1]
  q.append([x,y])
  while q:
    a,b = q.popleft()
    for k in range(4):
      nx, ny= a+dx[k], b+dy[k]
      if 0<= nx <n and 0 <= ny <m and matrix[nx][ny]==1:
        matrix[nx][ny]=0
        q.append([nx,ny])

t=int(input())
for _ in range(t):
  m,n,v = map(int,input().split())
  matrix=[[0]*m for _ in range(n)]
  q=deque()
  result=0
  for _ in range(v):
    a,b=map(int,input().split())
    matrix[b][a]=1
  for i in range(n):
    for j in range(m):
      if matrix[i][j]==1:
        matrix[i][j]=0
        bsf(i,j,q)
        result+=1
  print(result)