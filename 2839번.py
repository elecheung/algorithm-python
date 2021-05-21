n = int(input())
x=n//5
y=n%5
answer=0
while(1):
    if (x!=0)and(y%3!=0):
        y+=5
        x-=1
        #print('{} {}'.format(x,y))
    elif ((x==0) and (y%3!=0)):
        answer=-1
        break
    else:
        a=y//3
        answer=x+a
        break
print(answer)