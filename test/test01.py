while True:
    scroe = float(input('请输入你的分数：'))
    if scroe < 0 or scroe > 100:
        print("输入的分数请在规定范围内")
    elif scroe <= 60:
        print("E")
    elif scroe >= 60 and scroe <= 70:
        print("D")
    elif scroe >= 70 and scroe <= 80:
        print("C")
    elif scroe >= 80 and scroe <= 90:
        print("B")
    else:
        print("A")