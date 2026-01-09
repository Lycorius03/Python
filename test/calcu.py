store = {'apple': 6.5,'banana':4.0, 'orange': 5.8}
goods = input('请输入商品名称：')
if goods not in store:
    print('没有该商品')
else:
    while True:
        num = 0.0
        try:
            num = float(input('请输入购买数量（斤）：'))
            if num <= 0 :
                print('请重新输入一个正数')
                continue
            break
        except ValueError:
            print('请输入数字')
    total =store[goods] * num
    print(f"总价为:{total:.2f}")