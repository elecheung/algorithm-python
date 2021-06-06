v=int(input())
a=[]
sibal=[]
for i in range(v):
  a.append((i+1)**2)
for i in range(1,v):
  for j in range(i):
    if a[i]-a[j]==v:
      sibal.append(i+1)
      continue
print(sibal)