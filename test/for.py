#九九乘法表for循环语句
for i in range(1,10):
    for j in range(1,i+1):
        print(f"{j}*{i} = {j * i}",end=" ")
    print()
#1~10的累加和
total = 0
for x in range(1,11):
    total += x
print(f"1~10的累加和：{total}")
#九九乘法表while循环语句
i = 1
while i < 10:
    j = 1
    while j < i+1:
        print(f"{j}*{i} = {j * i}",end=" ")
        j += 1
    i += 1
    print()
