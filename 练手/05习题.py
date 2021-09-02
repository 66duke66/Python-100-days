"""
# 水仙花数也被称为超完全数字不变数、自恋数、自幂数、阿姆斯特朗数，它是一个3位数，该数字每个位上数字的立方之和正好等于它本身，例如：$1^3 + 5^3+ 3^3=153$。

sx = []
for num in range(100, 1000):
    low = num % 10
    mid = num //10 % 10
    high = num // 100
    if low ** 3 + mid ** 3 + high ** 3 == num:
        sx.append(num)
print(sx)

sx1 = []
for num in range(100, 1000):
    num = str(num)
    low = int(num[2])
    mid = int(num[1])
    high = int(num[0])
    num = int(num)
    if low ** 3 + mid ** 3 + high ** 3 == num:
        sx1.append(num)
print(sx1)



# 百钱白鸡：鸡翁一值钱五，鸡母一值钱三，鸡雏三值钱一。百钱买百鸡，问鸡翁、鸡母、鸡雏各几何？翻译成现代文是：公鸡5元一只，母鸡3元一只，小鸡1元三只，用100块钱买一百只鸡，问公鸡、母鸡、小鸡各有多少只？

for x in range(1, 21):
    for y in range(1, 31):
        z = 100 - x - y
        if x * 5 + y * 3 + z / 3 == 100 and x + y + z == 100:
            print(x, y, z)



# CRAPS赌博游戏:玩家第一次摇骰子如果摇出了7点或11点，玩家胜；玩家第一次如果摇出2点、3点或12点，庄家胜；其他点数玩家继续摇骰子，
# 如果玩家摇出了7点，庄家胜；如果玩家摇出了第一次摇的点数，玩家胜；其他点数，玩家继续要骰子，直到分出胜负。
import random
num = 0
while True:
    num = num + 1
    sex = random.randint(1, 7) + random.randint(1,7)
    sex1 = sex
    if num == 1:
        if sex == 7 or sex == 11:
            print("玩家胜")
            break
        elif sex == 2 or sex == 3 or sex == 12:
            print('庄家胜')
            break
    if num > 1:
        if sex == 7:
            print('庄家胜')
            break
        elif sex == sex1:
            print('玩家胜')
            break

# 生成斐波那契数列的前20个数。从第三个数开始，每个数都是它前面两个数的和，形如：1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...。
list = [1, 1]
for i in range(0,20):
    list.append(list[-1] + list[-2])
print(list)


# 找出10000以内的完美数。它的所有的真因子（即除了自身以外的因子）的和（即因子函数）恰好等于它本身如：6（$6=1+2+3$）和28（$28=1+2+4+7+14$）
lista = []
for a in range(1, 10001):
    lists = []
    for b in range(1, a):
        if a % b == 0:
            lists.append(b)
    if sum(lists) == a:
        lista.append(a)
print(lista)

# 输出100以内所有的素数。说明：素数指的是只能被1和自身整除的正整数（不包括1）。
for a in range(2, 101):
    b = 0
    for c in range(2,a):
        if a % c == 0:
            b += 1
    if b == 0:
        print(a)
"""






















































































