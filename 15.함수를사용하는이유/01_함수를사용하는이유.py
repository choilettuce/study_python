##함수를 사용하지 않은 경우
print("안녕하세요 상추님!!")
print("현재 서비스 사용기간이 30일 남았습니다")

print("안녕하세요 쫑민님!!")
print("현재 서비스 사용기간이 29일 남았습니다")

print("안녕하세요 쭈형님!!")
print("현재 서비스 사용기간이 8일 남았습니다")

## 함수를 사용한 경우
def print_message(name, data) :
    print("안녕하세요.", name, "님")
    print("현재 서비스 사용기간이 ",date,"일 남았습니다.")

print_message("상추", 30)
print_message("쫑민", 29)
print_message("쭈형", 7)
