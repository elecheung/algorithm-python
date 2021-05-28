t= int(input())
a = []

dp={
  0 : 1,
  1 : 1,
  2 : 2,
  3 : 6
}
def fact(n):
  if n not in dp:
    dp[n] = n*fact(n-1)
  return dp[n]
def com():
  n,m= map(int, input().split())
  result=fact(m)//(fact(m-n)*fact(n))
  return result

for _ in range(t):
  b = com()
  a.append(b)
for i in a:
  print(i)