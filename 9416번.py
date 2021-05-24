t=int(input())
fibo={
  1 : 1,
  2 : 1,
  3 : 1
}
def fb(n):
  if n not in fibo:
    fibo[n] = fb(n - 3) + fb(n - 2)
  return fibo[n]

for i in range(t):
  a=int(input())
  print(fb(a))