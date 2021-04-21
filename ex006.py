weather = int(input("오늘은 몇월입니까?"))

if 3 <= weather <= 5:
    print("봄입니다")
elif 6 <= weather <= 8:
    print("여름입니다")
elif 9 <= weather <= 11:
    print("가을입니다")
else:
    print("겨울입니다")