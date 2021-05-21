a=[]
b=[]
def sum(n):
    return n*(n+1)//2
num = int(input())
for i in range(0,num):
    a.append(input())
for i in a:
    n=0
    score =0
    for j in range(len(i)):
        if j != 0:
            if i[j-1] == i[j] =='O':
                n+=1
                if j == int(len(i)-1):
                    score+=sum(n)
            elif i[j] == 'X':
                score+=sum(n)
                n=0
            elif i[j] == 'O':
                n=1
                if j == int(len(i)-1):
                    score+=sum(n)                   
        else:
            if i[j] == 'O':
                n=1
                if j == int(len(i)-1):
                    score+=sum(n)
            else:
                n=0
        #print(n,score)
    b.append(score)
for i in range(0,num):
    print(b[i])