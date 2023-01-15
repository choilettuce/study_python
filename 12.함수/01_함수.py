## 기본함수 예시!

def sum (a,b) :
    result = a+b
    return result

x = sum(1,2)
y = sum(3,4)

print(x,y)

## 매개변수가 없는 함수!!
import random
def getRandomNumber () :
    number = random.randint(1,10)
    return number

z = getRandomNumber()
print(z)

## return 값이 없는 함수
name = "lettuce"
def printName (name) :
    print(name)

printName(name)

## 매개변수와 리턴값이 모두 없는 함수
def Sayhi() :
    print("bye ")

Sayhi()
