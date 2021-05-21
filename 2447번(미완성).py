
n=int(input())
a=[['*']*n for j in range(n)]
def star(n,list):
  if n==1:
    return list
  for i in range(n):
      if ((n//3)<= i <(2*n//3)):
        for j in range(n//3,2*n//3):
          list[i][j]=' '
  return star(n//3,list)
result=star(9,a)
for i in result:
 print(i)