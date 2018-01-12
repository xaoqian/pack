def hcf(x, y):
    '''该函数返回两个数的最大公约数'''
    if x < y:
        smaller = y
    else:
        smaller = x
    for i in range(1,smaller + 1):
        if(x % i == 0 ) and (y % i == 0):
            hcf == i
    return hcf
x = int(input('введите положительное число： '))
y = int(input('введите положительное число： '))
print(x, "和", y, '的最大公约数为', hcf(x, y))
hcf(x, y)