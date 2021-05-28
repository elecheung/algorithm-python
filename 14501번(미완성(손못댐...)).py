n= int(input())
t=[]
p=[]
dp={

}
for _ in range(n):
  a,b=map(int,input().split())
  t.append(a)
  p.append(b)
for i in range(n,-1,-1):
  if i==n:
    dp[i]=0
  elif p[i] not in dp:
    dp[i] = p[i]
for i in range(n-1,-1,-1):
  if i+t[i]>n:
    dp[i]=dp[i+1]
  else:  
    dp[i]=max(dp[i+1],p[i]+dp[i+t[i]])
print(dp[0])