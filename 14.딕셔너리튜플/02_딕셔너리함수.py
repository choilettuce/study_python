play_data = {
    'result' : '승리',
    'champ_name' : '비에고',
    'kill' : 13,
    'death' : 9,
    'assist' : 17
}

#keys()
for key in play_data.keys() :
    print(key)  #모든 키 출력

#values()
for value in play_data.values() :
    print(value) #벨류출력

#items()
for key, value in play_data.items() :
    print(key, value) #키벨류 출력
