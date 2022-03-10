from random import *

champ = [
    "레이너", "케리건", "아르타니스", "스완", "자가라", "보라준", "카락스", "아바투르",
    "알라라크", "노바", "스툽코프", "피닉스", "데하카", "한과 호너", "타이커스", "제라툴",
    "스텟먼", "멩스크"
    ]

prestige= randrange(0,4)

print("사령관 : ", choice(champ))
print(prestige,"위신")

a = input("엔터 쳐서 종료.... :    ")
