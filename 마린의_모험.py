# 마린의 모험
input("21xx년 x월 x일")
input("어느 한 마린이 한 행성에서 근무중이었다")

# 선택 오늘도 날씨가 좋구만 = 1    아 배고프다 시벌 = 0 
마린 = input("당신은 뭐라고 말하시겠습니까?")
마린 = int(마린)

if 마린:
    input("오늘도 날씨가 좋구만")
else:
    input("아 배고프다 시벌")

input("그러나 마린은 몰랐다 그것이 모험의 시발점이 될줄은...")

input("저 멀리서 거대한 재앙의 씨앗들이 흩뿌려지고 있다.")

# 선택 도망친다 = 1 싸운다 = 0
마린 = input("당신은 어떻하시겠습니까?")
마린 = int(마린)

if 마린: 
    input("도망친다")
    print("당신은 살아남으셨습니다")
    
    input("당신은 정신없이 도망치다 길을 잃었습니다")
    
    # 선택 왼쪽길 = 1 오른쪽길 = 0
    마린 = int(input("오른쪽길은 비명이 들려오고 왼쪽길은 조용합니다 당신은 어디로 가시겠습니까?"))
    if 마린:
        input("왼쪽길")
        input("왼쪽길에는 재앙들이 사람들을 모두 죽이고 당신을 기다리고 있었습니다")
        print("당신은 죽었습니다")
    else:
        input("오른쪽길")

    # 선택 안도와준다 = 1 도와준다 = 0
        마린 = int(input("오른쪽길로 들어가니 재앙에게서 도망치고있는 사람들을 발견했습니다\n그들을 도와주면 당신을 죽을지도 모릅니다 어떻하시겠습니까?"))
        if 마린:
            input("안 도와준다")
            input("도망치는 사람들중 영웅이 섞여있었습니다. 영웅이 죽었습니다.")
            print("당신은 죽었습니다")
        else:
            input("도와준다")
            input("사람들사이에 다친 영웅이 있었습니다. 영웅이 회복할때까지 당신은 시간을 끌었습니다")
            print("영웅이 재앙들을 모두 물리쳤습니다. 당신은 살아남았습니다")

            input("당신은 또다시 길을 떠납니다")
            input("............!")
            input(".....")
        
            # 선택 벗지않고 그대로 있는다 = 1 벗고 맨몸으로 다닌다 = 0
            마린 = int(input("수트의 배터리가 다 닳았습니다 당신은 어떻하시겠습니까?")
            if 마린:
                input("당신은 수트를 벗지 않았습니다")
                print("당신은 죽었습니다")
            else:
                input("당신은 수트를 벗었습니다")
                print("당신은 죽었습니다")
else:
    input("싸운다")
    print("당신은 재앙의 무리들에게 밟혀 죽었습니다")

