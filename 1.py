import turtle #画一个长方形，先需要直走right表示转的角度
turtle.forward(50)#表示直走的步数
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(100)


import turtle#画六边形，应为转过的角是外角六十度而不是内角120度
turtle.forward(100)
turtle.right(60)
turtle.forward(100)
turtle.right(60)
turtle.forward(100)
turtle.right(60)
turtle.forward(100)
turtle.right(60)
turtle.forward(100)
turtle.right(60)
turtle.forward(100)
turtle.right(60)

import turtle
turtle.forward(50)
turtle.right(120)
turtle.forward(50)
turtle.right(120)
turtle.forward(50)



import turtle
for i in range(90, 361, 90):
    turtle.right(i)
    for k in range(5, 26, 5):
        turtle.forward(k)
for i in range(90, 91):
    turtle.left(i)
    for k in range(5, 26, 5):
        turtle.forward(k)
turtle.left(90)
turtle.forward(150)