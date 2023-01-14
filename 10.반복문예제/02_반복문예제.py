## 사용자로부터 -1을 입력받으면 종료되는 프로그램을 작성

print("프로그램 시작")
num = int(input("종료하려면 -1을 입력하세요"))

## 첫번째 방법
# while num != -1 :
#     num = int(input("종료하려면 -1을 입력하세요"))

# print("프로그램 종료!!")

## 두번째 방법

while True :
    num = int(input("종료하려면 -1을 입력하세요"))
    if num == -1:
        break

# print("프로그램 종료!!")
