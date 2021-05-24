t=int(input())
color=[]
for i in range(t):
  color.append(list(map(int,input().split())))
for i in range(1,t):
  color[i][0] += min(color[i-1][1],color[i-1][2])
  color[i][1] += min(color[i-1][0],color[i-1][2])
  color[i][2] += min(color[i-1][0],color[i-1][1])
print(min(color[t-1][0],color[t-1][1],color[t-1][2]))