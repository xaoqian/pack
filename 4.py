import math
a = input('Введите координаты А через запятую: ')
b = input('Введите координаты В через запятую: ')
ak = a.split(',')
bk = b.split(',')
x1 = int(ak[0])#这里说的数字表示第几项
x2 = int(bk[0])
y1 = int(ak[1])
y2 = int(bk[1])
d1 = ((x2-x1)**2+(y2-y1)**2)**(1/2)
d2 = math.fabs(x2-x1) + math.fabs(y2-y1)
print('Евклидовово расстояние: ', d1)
print('Манхэттенское расстояние: ', d2)