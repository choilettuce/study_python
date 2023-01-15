## quiz2 사용자로부터 태어난 연도를 입력받으면, 현재 나이 출력

currentYear = int(2023)

birthYear = int(input("출생연도를 입력해주세요"))
age = int(currentYear-birthYear)

print("고객님의 현재 나이는"+ str(age) +"입니다")

## str(age)로 형변환을 해주지 않으면 int와 str을 더하기 할 수 없다고 오류가 확인된다.
## 파이썬은 str과 int의 합이 불가능!
