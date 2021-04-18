# 포켓몬 이름짓기
name = input(">당신의 포켓몬의 이름은?:")

if name:
    print("당신의 포켓몬의 이름은 {}입니다".format(name))

# 야생포켓몬의 등장

print("야생포켓몬 디아루가가 나왔다!! 가랏 {}!!".format(name))

b = input("{}는 무엇을 하겠습니까?".format(name))
b = int(b)

# a의 행동 싸운다=0 도망친다=1
# a의 기술 불대문자=2 불꽃세례=3 고속이동=4 바위깨기=5

if -1 < b < 1:
    print("싸운다")
    싸운다 = input("\n불대문자, 불꽃세례, 고속이동, 바위깨기\t")
    싸운다 = int(싸운다)

    if 싸운다 == 2:
        print("{}의 불대문자!! 400데미지".format(name))
    elif 싸운다 == 3:
        print("{}의 불꽃세례!! 200데미지".format(name))
    elif 3 < 싸운다 < 5:
        print("{}의 고속이동!! 회피 상승".format(name))
    else:
        print("{}의 바위깨기!! 500데미지".format(name))

else:
    print("{}는 도망쳤다".format(name))


