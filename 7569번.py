import sys
from collections import deque
m,n,h=map(int,input().split())
box=[list(list(map(int,input().split())) for _ in range(n)) for _ in range(h)]

def bsf(q,cnt):
  dx=[1,-1,0,0,0,0]
  dy=[0,0,1,-1,0,0]
  dz=[0,0,0,0,1,-1]
  while q:
    cnt+=1
    for _ in range(len(q)):
      a,b,c=q.popleft()
      for k in range(6):
        nx,ny,nz=a+dx[k], b+dy[k], c+dz[k]
        if 0<= nx <n and 0<= ny <m and 0<= nz <h and box[nz][nx][ny]==0:
          box[nz][nx][ny]=1
          q.append([nx,ny,nz])
  for b in box:
    for c in b:
      if 0 in c:
        return -1
  return cnt-1
q=deque()
for k in range(h):
  for i in range(n):
    for j in range(m):
      if box[k][i][j]==1:
        q.append([i,j,k])

print(bsf(q,0))