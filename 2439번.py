def find(a):  
    if 99<a<=1000:
        count=99
        for i in range(100,a+1):
            i=str(i)
            sum=0
            for j in i:
                sum+=int(j)
            if (sum/3) == int(i[1:2]):
                    count+=1
    else:
        count=a
    return count
b = int(input())
print(find(b))