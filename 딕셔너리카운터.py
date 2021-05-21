pets = [
    {'name':'구름', 'age' : 5},
    {'name':'초코', 'age' : 3},
    {'name':'아지', 'age' : 1},
    {'name':'호랑이', 'age' : 1}
]

print("# 우리 동네 애완 동물들")
for number in pets:
    print('{}{}'.format((number['name']),(number['age'])))
    
    
numbers = [1,2,6,8,4,3,2,1,9,5,4,9,7,2,1,3,5,4,8,9,7,2,3]
counter={}
'''i=0
j=0
for number1 in numbers:
    for j in numbers: 
       if number1 == j:
           i+=1
       counter[j]=i
       i=0
print(counter)'''

for number in numbers:
    if number in counter:
        counter[number] +=1
    else:
        counter[number] =1
        
print(counter)


