def fibonachi(n):
  a={
    0 : 0,
    1 : 1,
    2 : 1
  }
  if n<=1:
    return n
  if n not in a:
    b= a[n-1] +a[n-2]
    a[n]=b
  return fibonachi(n-1)+fibonachi(n-2)

a=fibonachi(int(input()))
print(a)