import random


# 水仙花数也被称为超完全数字不变数、自恋数、自幂数、阿姆斯特朗数，它是一个3位数，该数字每个位上数字的立方之和正好等于它本身，例如：$1^3 + 5^3+ 3^3=153$。
def shuixianhuashu1(a, b):
    """
    求水仙花数
    :param a: 起始值
    :param b: 终止值
    :return: 水仙花数（列表）
    """
    sx = []
    for num in range(a, b + 1):
        low = num % 10
        mid = num // 10 % 10
        high = num // 100
        if low ** 3 + mid ** 3 + high ** 3 == num:
            sx.append(num)
    print(sx)
    return sx


def shuixianhuashu2(a=100, b=10001):
    """
    求水仙花数
    :param a: 起始值
    :param b: 终止值
    :return: 水仙花数（列表）
    """
    sx1 = []
    for num in range(a, b + 1):
        num = str(num)
        low = int(num[2])
        mid = int(num[1])
        high = int(num[0])
        num = int(num)
        if low ** 3 + mid ** 3 + high ** 3 == num:
            sx1.append(num)
    print(sx1)


# 百钱百鸡：公鸡5(a)元一只，母鸡3(b)元一只，小鸡1/3(c)元一只，用100(f)块钱买100(g)只鸡，问公鸡x、母鸡y、小鸡z各有多少只？
def baiqianbaiji(a, b, c, f, g):
    """
    :param a: 公鸡单价
    :param b: 母鸡单价
    :param c: 小鸡单价
    :param f: 采购金额
    :param g: 目标数量
    :return: 公鸡，母鸡，小鸡
    """
    for x in range(0, f // a):
        for y in range(0, f // b):
            z = 100 - x - y
            if x * a + y * b + z * c == f and x + y + z == g:
                print(x, y, z)


# CRAPS赌博游戏:玩家第一次摇骰子如果摇出了7点或11点，玩家胜；玩家第一次如果摇出2点、3点或12点，庄家胜；其他点数玩家继续摇骰子，
# 如果玩家摇出了7点，庄家胜；如果玩家摇出了第一次摇的点数，玩家胜；其他点数，玩家继续要骰子，直到分出胜负。


def craps():
    """
    :return: 赌局结果
    """
    num = 0
    while True:
        num = num + 1
        sex = random.randint(1, 7) + random.randint(1, 7)
        sex1 = sex
        if num == 1:
            if sex == 7 or sex == 11:
                result = "玩家胜"
                break
            elif sex == 2 or sex == 3 or sex == 12:
                result = "庄家胜"
                break
        if num > 1:
            if sex == 7:
                result = "庄家胜"
                break
            elif sex == sex1:
                result = "玩家胜"
                break
    return result


# 生成斐波那契数列的前20个数。从第三个数开始，每个数都是它前面两个数的和，形如：1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...。
def fbnqsl(fbnq):
    """
    :param fbnq: 目标数列长度
    :return: 斐波那契数列(列表)
    """
    list1 = [1, 1]
    for i in range(0, fbnq):
        list1.append(list1[-1] + list1[-2])
    return list1


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
    for c in range(2, a):
        if a % c == 0:
            b += 1
    if b == 0:
        print(a)
