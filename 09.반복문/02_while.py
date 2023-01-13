## while문을 for문으로 전환
for count in range(5) :
    print(count, "번째 반복입니다.")

count = 0
while count>5 :
    print(count,"번째 반복입니다.")
    count = count+1

## while 조건 :  =>>조건식이 true일때 명령블록 시작
##  명령블록 
## for -> 정한 횟수만큼 반복
## while -> 조건을 만족하지 않을 때 까지 반복