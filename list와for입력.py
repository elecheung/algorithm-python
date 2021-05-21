lol=[[1,2,3],[4,5,6,7],[8,9],]


for number in lol:
  for number2 in number :
      print(number2)
      
numbers = [1,2,3,4,5,6,7,8,9]
output = [[],[],[]] 

for number3 in numbers:
    output[(number3-1)%3].append(number3)
    
print(output)