## for 변수 in 리스트 :
##  명령블록

for a in [1,2,3,4] :
    print(a)

## 예시2
names = ["티모","리신","이즈리얼"]
for name in names :
    print(name)

## 조건문이랑 결합 반복문
greetings = ["hi","hello","bye"]
for greeting in greetings :
    if greeting == "hi" : 
        print(greeting +" "+ "everyone")
    elif greeting == "hello" :
        print(greeting +" "+ "my name is lettuce")
    elif greeting == "bye" :
        print(greeting +" "+ "see you later")


## for + range 사용법
# range(10) -> 0~9까지 순서열을 반환 

for i in range(60) :
    print(i+1,"분")


for i in range(12):
    print(i+1,"월")

## range(시작숫자, 끝숫자+1)
## range(1,10) => 1부터 9까지의 숫자!!

## range(1,10,2) => 1,3,5,7,9
## range(시작숫자, 끝숫자+1, 단계)

for i in range(1,11) :
    print(i,"번째 페이지입니다.")

