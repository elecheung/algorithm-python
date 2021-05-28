n= int(input())
dp={
  1 : 1,
  2 : 1,
  3 : 2,
  4 : 3
}
def pinary(n):
  if n not in dp:
    dp[n]=pinary(n-1)+pinary(n-2)
  return dp[n]
print(pinary(n))