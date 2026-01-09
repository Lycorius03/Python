while True:
    h = float(input("请输入你的身高："))
    w = float(input("请输入你的体重："))
    BMI = w / (h * h)
    if BMI < 18.5:
        print("偏瘦，体重太轻了，要增加营养哦")
    elif BMI >= 18.5 and BMI < 24:
        print ("正常，您的身体翡翠健康，太棒啦")
    elif BMI >= 24 and BMI < 28:
        print("偏胖，规律作息、合理饮食，会变得健康哦")
    else:
        print("肥胖，保持健康身体是爱护自己的表现，要运动起来呀")