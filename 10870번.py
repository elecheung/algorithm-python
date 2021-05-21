def finbonachi(n):
  if n<=1:
    return n
  return finbonachi(n-1)+finbonachi(n-2)
a=finbonachi(int(input()))
print(a)