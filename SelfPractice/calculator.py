# 숫자 입력 받아서 두 숫자의 계산 만들기
# 계산 결과가 저장되지 않는다

a = int(input('숫자를 입력해 주세요:'))
b = int(input('숫자를 입력해 주세요:'))
c = input('연산자를 입력해 주세요:')
def input_cal(a,b,c):
    if c == '+':
        return a+b
    elif c == '-':
        return a-b
    elif c == '*':
        return a*b
    elif c == '/':
        return a/b
print(input_cal(a,b,c))