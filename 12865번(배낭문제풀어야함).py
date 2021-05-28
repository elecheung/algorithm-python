n,k=map(int,input().split())
dp={
}
for _ in range(n):
  a=list(map(int,input().split()))
for i in range(n):
  dp[a[i][0]]=a[i][1] 
print(dp)