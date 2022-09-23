from dis import dis
import turtle,random,string
sc= turtle.Screen()
pen = turtle.Turtle()
wn=turtle.Screen()
#小格子宽度
distance =50
grid=[[]]

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
        x = random.randrange(0,12)
        y = random.randrange(0,12)
        drawFill(x*distance-300,y*distance-300,distance,'black')
        grid[x][y]=1

def initStartEnd():
    pen.speed(0)
    drawFill(-300,-300,distance,'green')
    drawFill(200,250,distance,'red')


def initGrid(size):
    x = []
    for i in range(size):
        x.append(0)

    for i in range(size):
        grid.insert(i,x)

if __name__ == "__main__" :
    initGrid(12)
    wn.screensize()
    wn.setup(width = 1.0, height = 1.0)
    turtle.onclick(turn)
    pen.speed(0)
    sc.setup(650,650)
    drawFast(-300,-300,12)
    initStartEnd()
    setObstacles(5)
    pen.hideturtle()
turtle.done()


