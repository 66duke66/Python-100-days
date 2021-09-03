# 练习1：实现计算求最大公约数和最小公倍数的函数。
def gongyueshu(x, y, z):
    """
    公约数
    :param x:
    :param y:
    :param z: 模式  1：最大公约数  2：公约数数列（大到小）
    :return: 1：最大公约数  2：公约数数列（大到小）
    """
    global gys
    if x > y:
        gys0 = x
    else:
        gys0 = y
    if z == 1:
        while gys0 > 0:
            x0 = x % gys0
            y0 = y % gys0
            if x0 == 0 and y0 == 0:
                gys = gys0
                break
            gys0 -= 1
    elif z == 2:
        gyslist = []
        while gys0 > 0:
            x0 = x % gys0
            y0 = y % gys0
            if x0 == 0 and y0 == 0:
                gyslist.append(gys0)
            gys0 -= 1
        gys = gyslist
    return gys

# 练习2：实现判断一个数是不是回文数的函数。
def huiwenshu():
