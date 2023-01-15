# 1. 승패여부
# 2. 챔피언이름
# 3. 킬
# 4. 데스
# 5. 어시스트

# 변수를 사용할 때
result = "승리"
champ_name = "비에고"
kill = 13
death = 9
assist = 17

# 리스트를 사용할때
# play_data = ['승리', '비에고', 13, 9, 17]
# play_data2 = ['승리', '비에고', 13, 9, 17]

# 딕셔너리 사용할때 
play_data = {
    'result' : '승리',
    'champ_name' : '비에고',
    'kill' : 13,
    'death' : 9,
    'assist' : 17
}

## 딕셔너리 = 키와 값의 쌍으로 이루어진 자료형
# 자바스크립트의 object

## 딕셔너리 접근법
x = play_data['result']
y = play_data['kill']

print(x,y)

# 기존값 변경
play_data['result'] = '패배'
print(play_data['result'])

#새로운 키,값 추가
play_data['level'] = 18
print(play_data)

#데이터 삭제
del play_data['champ_name']
print(play_data)