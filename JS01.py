rawscore=list(map(int,input().split()))
convfac=list(map(int,input().split()))

def round(a,b):
  if (a%b)/b>=0.5:
    return (a//b)+1
  else:
    return a//b

a=[]
for i in range(len(rawscore)):
  a.append(round(rawscore[i],convfac[i]))
sum=0
for i in a:
  sum+=i
print(sum)