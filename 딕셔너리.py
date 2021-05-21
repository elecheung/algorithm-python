dictionary = {
    '이름' : "구름",
    '종족' : '강아지'
    }

dictionary['이름']
print(dictionary.get('이름'))
print(dictionary['이름'])

print(dictionary.get('나이')) #없는값이 들어가면 None의 출력을 한다

if '나이' in dictionary:
    print(dictionary['나이']) #없는 값이 들어가면 오류가 들어감으로 확인해 주어야 한다.
else:
    print("없는 키 입니다.")