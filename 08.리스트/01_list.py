## 리스트 생성하기
## 인덱스는 0부터 시작한다!!!
animals = ["사자", "호랑이", "강아지","고양이"]
print(animals)

## 데이터 접근하기

name = animals[0]
print(name)

## 데이터 추가하기
# append method 활용하기!
animals.append("오리")
print(animals)

## 데이터 삭제하기
# del 키워드 이용하여 del 리스트[인덱스]로 이용
# del animals[-1] => 마지막 데이터 삭제
del animals[1] 
print(animals)

## 리스트 슬라이싱
print(animals[0:3])

## 리스트 길이확인
# len method 활용하기!
print(len(animals))
# print(animals.len) -> 이렇게는 안되네...

## 리스트 정렬
# 리스트.sort() 메소드 활용하기! 오름차순으로 정렬!
animals.sort()
print(animals)

animals.sort(reverse = True) ## 내림차순!!
print(animals)






