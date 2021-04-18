if <조건>:
    조건이 참일 때 실행할 문장


들여쓰기 입력하기: Tap
들여쓰기 제거: Shift + Tap 혹은 BackSpace

예를들면 이런식

number = input("정수 입력")
number = int(number)

if number > 0:
    print("양수입니다")
if number == 0:
    print("0입니다")
if number < 0:
    print("음수입니다")

if 조건:
    조건이 참일 때 실행할 문장
else:
    조건이 거짓일 때 실행할 문장

# 봄 여름 가을 겨울    
else + if = elif

if 3 <= now.month <= 5:
    print("이번 달은 {}월로 봄입니다!".format(now.month))
elif 6 <= now.month <= 8:
    print("이번 달은 {}월로 여름입니다!".format(now.month))
elif 9 <= now.month <= 11:
    print("이번 달은 {}월로 가을입니다!".format(now.month))
else:
    print("이번 달은 {}월로 겨울입니다!".format(now.month))

elif, else를 사용하게 되면 여러개여도 마지막 구문을 사용하지 않아도 되서 더 효율적이다.


