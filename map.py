import turtle
sc= turtle.Screen()
pen = turtle.Turtle()
#小格子宽度
distance =50

#正方形
def draw():
    for i in range(4):
        #向当前画笔方向移动distance像素长度
        pen.forward(distance)
        pen.left(90)
    pen.forward(distance)

def draws(x,y,size):
    for i in range(size):
        draw()
        pen.goto(-300+i,y)
        pen.setx(distance*i)
        print (pen.position)
        draw()


def turn(x, y):
# 打印当前坐标
   print('x=', x, 'y=', y)
# 打印当前方向
   print(turtle.heading())


if __name__ == "__main__" :
    turtle.onclick(turn)
    pen.speed(1)
    sc.setup(600,600)
    #pen.up()
    pen.goto(-300,-300)
    #pen.down()
    draws(-300,-300,8)
    pen.hideturtle()
turtle.done()


