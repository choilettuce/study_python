## 제어문은 크게 조건문과 반복문으로 나뉜다.

## 조건문
## if 조건식 : 
#   조건식이 참일 때 실행되는 명령
## 들여쓰기가 중요!
# else :
#   조건식이 거짓일때 실행되는 명령


## 만약에 적과의 거리가 200m 이상이라면: 저격소총을 쏜다
## 그게 아니라면 : 돌격소총을 쏜다.

distance = 190

if distance >=200 :
    print("저격소총 쏘기!")
else : 
    print("돌격소총 쏘기!")