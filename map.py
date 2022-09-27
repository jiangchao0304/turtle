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

#设置随机障碍
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

#计算最短路径
def bfs(begin,end,graph):
    dir = [[0, 1],[1, 0],[0, -1], [-1, 0]]  # 四个方向，D,L,R,U 
    queue =[]
    visit = []
    result = []
    queue.append(begin)
    visit.append(begin)
    while queue:
        node = queue.pop(0)
        x=node[0]
        y=node[1]
        for i in dir:
            if x+i[0] < len(graph)-1 and y+i[1]< len(graph)-1  and x+i[0]>=0  and y+i[1]>=0:
               if [x+i[0],y+i[1]] not in visit:
                  visit.append([x+i[0],y+i[1]]) 
                  queue.append([x+i[0],y+i[1]])
                  print  ([x+i[0],y+i[1]]) 
                  #queue.insert(0,[x+i[0],y+i[1]]) 
        result.append(node)         
        #print(visit)
        #print(queue)
        print (11111111)

def initGrid(size):
    x = []
    for i in range(size):
        x.append(0)

    for i in range(size):
        grid.insert(i,x)

if __name__ == "__main__" :
    initGrid(3)
    bfs([0,0],[3,3],grid)
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


