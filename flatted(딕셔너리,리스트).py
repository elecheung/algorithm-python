character = {
    'name' : '기사',
    'level' : 12,
    'item' : {
        'sword' : '불꽃의 검',
        'armor' : '풀플레이트'
        },
    'skill' : ['베기','세게 베기','이주 세게 베기']
    }

for key in character:
   if type(character[key]) is dict: #character[key]의 타입이 dictionary이면
       for k in character[key]:
           print('{} : {}'.format(k,character[key][k]))
   elif type(character[key]) is list:
       for item in character[key]:
           print('{} : {}'.format(key,item))
   else:
       print('{} : {}'.format(key,character[key]))
       

       ''' if not key == 'item':
        print(key,':',character[key])
    elif key == 'item':
        print(key['item'],':',character['item']['sword'])'''
    