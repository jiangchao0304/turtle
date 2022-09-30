from dis import dis
import turtle,random,string
sc= turtle.Screen()
pen = turtle.Turtle()
wn=turtle.Screen()
#小格子宽度
distance =50
grid = [[]]

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
    pathDic={}
    pathResult=[end]
    queue.append(begin)
    visit.append(begin)
    while queue:
        node = queue.pop(0)
        x=node[0]
        y=node[1]
        for i in dir:
            #判断边界
            if x+i[0] < len(graph) and y+i[1]< len(graph)  and x+i[0]>=0  and y+i[1]>=0:
               if  graph[x+i[0]][y+i[1]]==1:
                   continue

               if [x+i[0],y+i[1]] not in visit:
                  visit.append([x+i[0],y+i[1]]) 
                  queue.append([x+i[0],y+i[1]])
                  pathDic[x+i[0],y+i[1]] = node
                  print  ([x+i[0],y+i[1]]) 
                  #queue.insert(0,[x+i[0],y+i[1]]) 
    #倒叙遍历出路径
    lastXYParent= pathDic.get(list(pathDic.keys())[-1])
    while lastXYParent[0]!=0 or lastXYParent[1]!=0:
           pathResult.insert(0,lastXYParent)
           lastXYParent = pathDic.get((lastXYParent[0],lastXYParent[1]))
    print (pathResult)       
    return pathResult

def drawBfs(begin,end,graph):
    pathResul= bfs(begin,end,graph)
    for i in range(0, len(pathResul)):
      drawFill(pathResul[i][0]*distance-300,pathResul[i][1]*distance-300,distance,'blue')
      print (i, pathResul[i])
    print('完成')
    





def initGrid(lsize,wsize):
    global grid 
    grid = [[0 for x in range(lsize)] for x in range(wsize)]
    #wn.screensize()
    #wn.setup(width = 1.0, height = 1.0)
    #turtle.onclick(turn)
    pen.speed(0)
    #窗体大小
    turtle.setup(width=800,height=800, startx=0, starty=0)
    turtle.screensize(800, 600)  
    #sc.setup(600,600)
    drawFast(-300,-300,12)
    initStartEnd()
    setObstacles(30)


if __name__ == "__main__" :
    initGrid(12,12)
    drawBfs([0,0],[11,11],grid)
    pen.hideturtle()
turtle.done()


