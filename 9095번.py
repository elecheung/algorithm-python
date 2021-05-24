t=int(input())
a=[]
c={
  1 : 1,
  2 : 2,
  3 : 4
}  
for _ in range(t):
  a.append(int(input()))
def num(n):
  if n not in c:
    c[n]=num(n-1)+num(n-2)+num(n-3)
  return c[n]
for i in a:
  print(num(i))