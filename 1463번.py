n=int(input())
dic={
  1:0,
  2:1,
  3:1,
  4:2
}
count=0
def mini(n):
  global count
  if n not in dic:
    dic[n]=mini(n)
  if n%3==0:
    mini(n)=mini(n//3)+1
  elif n%3==1:
    count+=1
    mini(n-1)
  else:
    count+=1
    mini(n-1)

print(mini(n))