## 프로그램 사용자로부터 가방과 시계의 금액을 입력받는다.
## 조건에 따라 합계 금액을 계산하고, 합계금액을 출력한다.
# 1. 합계 금액이 10만원 이상이면 할인률 30%
# 2. 합계금액이 5만원 이상 10만원 미만이면 할인률 20%
# 3. 합계금액이 5만원 미만이면 할인률 10%

BagPrice = int(input("가방금액을 입력하세요>>>"))
WatchPrice = int(input("시계금액을 입력하세요>>>"))

TotalPrice = int(BagPrice + WatchPrice)

if TotalPrice >= 100000 :
   print(TotalPrice * 0.7)
elif TotalPrice >= 50000 :
    print(TotalPrice * 0.8)
else :
    print(TotalPrice * 0.9)