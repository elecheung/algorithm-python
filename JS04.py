string=list(map(str,input().split()))
a=0
count=0
for i in string:
  a =max(a,len(i))
for i in string:
  if a != int(len(i)):
    c = ' '*(a -len(i))
    string[count]= c + i
  count+=1
print(string)