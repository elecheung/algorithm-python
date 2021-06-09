import sys
from collections import deque
finder,hider=map(int,input().split())

q=deque()
road=[0] * 100001
def bfs(hider,q):
  while q:
    a=q.popleft()
    if a==hider:
      return road[a]
    for nx in (a+1,a-1,2*a):
      if 0<= nx <= 100001 and road[nx]==0:
        road[nx]=road[a]+1
        q.append(nx)
q.append(finder)
print(bfs(hider,q))
