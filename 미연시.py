# 미연시 시작
print("티랜드가 밖으로 나갔다. 밖에는 예쁜 여자친구가 있었다.")

티랜드 = input("티랜드는 무엇을 하겠습니까?\t")
티랜드 = int(티랜드)

# 첫번째 행동 밖으로 나간다 = 1, 방으로 다시 들어간다 = 2, 여친과 신나게 놀기 = 3
# 두번째 행동 나 친구만나러가 = 4, 사 살려줘!! = 5, 나도 사랑해~!! = 6

if 티랜드 == 1:
    print("밖으로 나간다\t")
    여자친구 = input("자기야 어디가?\t")
    여자친구 = int(여자친구)
    if 여자친구 == 4:
        print("나 친구만나러가")
    elif 4 < 여자친구 < 6:
        print("사 살려줘!!")
    else:
        print("나도 사랑해~!!")
    
elif 2 < 티랜드 < 3:
    print("방으로 다시 들어간다\t")
    여자친구 = input("자기야 어디가? 라고 하며 여자친구가 문을 턱 잡으며 칼을 들이댄다\t")
    여자친구 = int(여자친구)
    if 여자친구 == 4:
        print("나 친구만나러가")
    elif 4 < 여자친구 < 6:
        print("사 살려줘!!")
    else:
        print("나도 사랑해~!!")

else:
    print("여친과 신나게 논다\t")
    여자친구 = input("자기야 사랑해~!\t")
    여자친구 = int(여자친구)
    if 여자친구 == 4:
        print("나 친구만나러가")
    elif 4 < 여자친구 < 6:
        print("사 살려줘!!")
    else:
        print("나도 사랑해~!!")


