def банк():
    s = int(input('введите число вклада: '))  # 第一年得到的钱
    b = int(input('с какого года: '))
    c = int(input('в каком году: '))
    d = []  # все деньги
    e = s * 0.1  # 第一年应该捐的款
    g = c - b + 1
    if b < c:
        for i in range(0, g):
            s = s+(s*0.1)
            e = 0.1*s
            d = s-e
            print(d)
банк()
