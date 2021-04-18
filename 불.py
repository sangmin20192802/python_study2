# 비교 연산자
print(10 == 100) # 거짓
print(10 != 100) # 참
print(10 > 100 ) # 거짓
print(10 < 100 ) # 참
print(10 >= 100) # 거짓
print(10 <= 100) # 참
프로그래밍 단골 문제
X = 20
10< X < 20

논리 연산자
# 단항 연산자
not
not True # False
not False # True
# 이항 연산자 (자료 두 개에 적용하는 연산자 10 + 10또한 이항연산자이다.)
and
True and True # 그리고
or
True or True # 또는

사과 그리고 배 : 사과 + 배 둘다 들고와...! (A 그리고 B = A와 B를 둘다 하라는 의미)
사과 또는 배 : 사과와 배 중에 아무거나 들고와...! (A 또는 B = A와 B 둘 중에 하나만이라는 의미)

사과 그리고 똥 : 사과 + 똥 -> 명령 거부
사과 또는 똥 : 명령 OK

사과 and 사과 : OK # True and True = True
사과 and 똥 : X # True and False = False
똥 and 사과 : X # False and True = False
똥 and 똥 : XX # False and False = False

사과 or 사과 : OK # True or True = True
사과 or 똥 : OK # True or False = True
똥 or 사과 : OK # False or True = True
똥 or 똥 : X # False or False = False