# 클래스 : like 제품의설계도
# 객체 : 설계도로 만든 제품
# 속성 : 클래스 안의 변수
# 메서드 : 클래스 안의 함수
# 생성자 : 객체를 만들 때 실행되는 함수
# 인스턴스 : 메모리에 살아있는 객체

## 클래스 정의
# class 클래스이름 :
#   def 메서드이름(self):   -> self에는 객체 자신이 들어간다
#       명령블록

## 사용법
# 객체 = 클래스이름()
# 객체.메서드()

# shark = Monster()
# shark.say()

## 생성자
class Monster:
    def __init__(self, name, age): ## 생성자에 꼭 언더바 두개씩!! 안하면 오류
        self.name = name
        self.age = age
    def say(self):
        print(f"나는 {self.name} {self.age}살입니다")

shark = Monster("상어",7)
shark.say()
wolf = Monster("늑대",4)
wolf.say()