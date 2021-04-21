bool(??) # True # False?
# None
0 + 0.0 = False 그냥 0이면 False  라고 생각하면 됨
빈 컨테이너("", b"", [], (), {}) = False  
순서대로 빈 문자열, 빈 바이트열, 빈 리스트, 빈 튜플, 빈 딕셔너리

예를들어 
message = ""
if message:
    print("처리를 한다")
else:
    print("0이 나왔습니다")

여기에서 보통 개발자들은 !=를 생략하고 if message: 로 한다. 
이게 생락하면 자동으로 '불' 처리 됨

# 숫자
number = 0 # 나중에!

if number:
    # 이런 처리
    pass
else:
    # 이런 처리
    pass

이처럼 프로그래밍 전체 골격을 잡아놓고, 
내부에 처리할 내용은 나중에 만들고자 할 때 pass라는 키워드를 입력해둡니다.

pass 키워드 자리에 raise NotImplementedError 를 넣게되면 "아직 구현되지 않은 부분이에요"
라는 오류를 강제로 발생시킬수 있다. pass를 쓰면 나중에 까먹을수도 있기 때문이다