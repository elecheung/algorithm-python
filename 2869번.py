a,b,v=map(int,input().split())
day=(v-b)/(a-b)
if (day == int(day)):
    day=day
else:
    day+=1
print('{}'.format(int(day)))