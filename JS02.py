n= int(input())
a = []
count=len(str(n))
for i in str(n):
  if int(i)>7:
    for i in range(count):
      a.append(7)
    break
  elif int(i)==7:
    a.append(7)
  elif int(i)>=4:
    a.append(4)
  else:
    a.append(7)
  count-=1
for i in a:
  print(i)