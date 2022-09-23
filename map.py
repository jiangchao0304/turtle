from dis import dis
import turtle,random,string
sc= turtle.Screen()
pen = turtle.Turtle()
wn=turtle.Screen()
#小格子宽度
distance =50




#正方形
def draw(x,y,dist):
    drawFill(x,y,dist,'#ffffff')

#颜色填充 green or #ffffff
def drawFill(x,y,dist,fillcolor):
    pen.begin_fill()
    pen.fillcolor(fillcolor)
    pen.up()
    pen.goto(x,y)
    pen.down()
    for i in range(4):
        #向当前画笔方向移动distance像素长度
        pen.forward(dist)
        pen.left(90)
    pen.end_fill()            

def draws(x,y,size):
      nextX =x;
      nextY= y;
      for yIndex in range(size):
        for xIndex in range(size):
           draw(nextX,nextY,distance)
           nextX = x + distance* (xIndex+1)
        nextX = x   
        nextY = y + distance* (yIndex+1) 



def drawFast(x,y,size):
    nextX =x;
    nextY= y;
    for yIndex in range(size+1):
        pen.up()
        pen.goto(nextX,nextY)
        pen.down()
        pen.forward(distance*size+1)
        nextY = y + distance* (yIndex+1)
    nextX =x;
    nextY= y;
    pen.left(90)
    for xIndex in range(size+1):
        pen.up()
        pen.goto(nextX,nextY)
        pen.down()   
        pen.forward(distance*size+1)
        nextX = x + distance* (xIndex+1)
    pen.right(90)  
    
def turn(x, y):
# 打印当前坐标
   print('x=', x, 'y=', y)


def setObstacles(count):
    for i in range(count):
        x = random.randint(1,11)*distance
        y = random.randint(1,11)*distance
        drawFill(x-300,y-300,distance,'black')

def initStartEnd():
    pen.speed(0)
    drawFill(-300,-300,distance,'green')
    drawFill(200,250,distance,'red')

if __name__ == "__main__" :
    wn.screensize()
    wn.setup(width = 1.0, height = 1.0)
    turtle.onclick(turn)
    pen.speed(0)
    sc.setup(650,650)
    drawFast(-300,-300,12)
    initStartEnd()
    setObstacles(30)
    pen.hideturtle()
turtle.done()


