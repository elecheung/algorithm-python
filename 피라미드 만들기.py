a= int(input('숫자를 입력하세요.'))

for i in range(0,a+1):
    print(' '*(a-i),'*'*(2*i-1),' '*(a-i))

