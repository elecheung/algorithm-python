t=int(input())
def bsf(m,n,mat,visit):
  dx=[1,-1,0,0]
  dy=[0,0,1,-1]
  queue=[[0,0]]
  if mat[0][0]==1:
    visit[0][0]=1
  while queue:
    x=queue[0][0]
    y=queue[0][1]
    queue.pop(0)
    for k in range(4):
      nx, ny = x+dx[k] ,y+dy[k]
      if 0<= nx < n  and 0<= ny <m and visit[nx][ny]==0 and mat[nx][ny]==1:
        visit[nx][ny]=1
        mat[nx][ny]=0
        queue.append([nx,ny])

ans=[]
cnt=0
for _ in range(t):
  m,n,v = map(int,input().split())
  mat=[[0]*m for _ in range(n)]
  visit=list([0]*m for _ in range(n))
  for _ in range(v):
    from_n,to_n = map(int,input().split())
    mat[to_n][from_n]=1
  for i in range(n):
    for j in range(m):
      if mat[j][i]==1:
        ans.append(bsf(j,i,mat,cnt+1))
  print(len(ans))