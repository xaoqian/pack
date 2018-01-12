a = int(input())
b = int(input())
def euclidean_algorithm(a,b):
    """辗转相除法求最大公约数"""
    if a < b:
        a, b = b, a
    r = 1
    while r != 0:
        r = a % b
        a = b
        b = r
    return a
euclidean_algorithm(a,b)

def gengxianjiansun(a, b):
    """《九章算术》中的“更相减损术”"""
    if a < b:
        a, b = b, a
    # 初始化差的集合为空
    divisors = []
    # 初始化最大公约数为1
    num = 1

    # 第一步：判断是否都是偶数
    if a % 2 == 0 and b % 2 == 0:
        a, b = a/2, b/2
        num *= 2

    # 第二步：更替相减
    r = a - b
    while r not in divisors:
        divisors.append(r)
        a = max(b, r)
        b = min(b, r)
        r = a - b
    return num * r



if __name__ == "__main__":
    print(euclidean_algorithm(8, 9))
    print(gengxianjiansun(8, 20))

