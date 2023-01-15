# 1. 로또번호 6개 생성
# 2. 로또 번호는 1~45까지의 랜덤한 번호
# 3. 6개의 숫자 모두 달라야한다
# 4. 로또 번호 생성함수를 작성하고 사용한다.
import random

def lotto () :
        num1 = random.randint(1, 45)
        num2 = random.randint(1, 45)
        num3 = random.randint(1, 45)
        num4 = random.randint(1, 45)
        num5 = random.randint(1, 45)
        num6 = random.randint(1, 45)
        if num1 != num2 != num3 != num4 != num5 != num6 :
            print(num1, num2, num3, num4, num5, num6)

lotto()