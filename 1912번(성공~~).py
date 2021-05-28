n= int(input())
a=list(map(int,input().split()))
dp={

}
for i in range(n):
  if i == 0:
    dp[i]=a[i]
  else:
    if dp[i-1]<0:
      dp[i]=a[i]
    else:
      dp[i]=dp[i-1]+a[i]
b=max(dp.values())
print(b)
