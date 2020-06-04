# -*- coding: utf-8 -*-
"""
Created on Thu May 21 17:12:24 2020

@author: 76754
"""


# 辗转相除法
def max_devide(m,n):
    while 1:
        r=m%n
        if r==0:
            return n
        else:    
            m,n=n,r
    return n

max_devide(5,2)

# 检查素数
#1 一个数若可以进行因数分解，那么分解时得到的两个数一定是一个小于等于sqrt(n)，一个大于等于sqrt(n)
def check_prime(n):
    n=int(input("Please enter an integer:"))
    for i in range(2,int(n**0.5)+1):
        if n % i==0:
            print(f"{n} is not a prime")
            break
    else:
        print(f"{n} is a prime")

check_prime(5)

# 打印三角形
n=5
for i in range(n):
    print(i*'*')
    
# 变位词
    
def check(word1, word2):#O(N)
    for i in word1:
        if i not in word2:
            return False
    return True
check('python','typhos')


def check(word1, word2):#O(NlogN)
    list1,list2=list(word1),list(word2)
    list1.sort()
    list2.sort()
    pos=0
    while pos<len(list1):
        if list1[pos]!=list2[pos]:
            return False
        pos+=1
    return True
check('python','typhon')

def check(word1, word2):#O(N)
    word1=list(word1)
    dict1={}
    for value in word1:
        dict1[value]=word1.count(value)
    word2=list(word2)
    dict2={}
    for value in word1:
        dict2[value]=word2.count(value)
    if dict1==dict2:
        return True
    else:
        return False
        
def check(word1, word2):#O(N) 引入字母表通过在其对应位置上加一
    c1=[0]*26
    c2=[0]*26
    for i,value in enumerate(word1):
        pos=ord(word1[i])-ord('a')
        c1[pos]=c1[pos]+1
    for i,value in enumerate(word2):
        pos=ord(word2[i])-ord('a')
        c2[pos]=c2[pos]+1
    if c2==c1:
        return True
    else:
        return False

# 线性结构：有序数据项的集合，每个数据项都有唯一的前驱和后继
#1.  stack栈  2.queue 队列 3. 双端队列  deque  4.列表 List   
# 数据项的增减方式不同        
        
    
    
# stack 栈：数据项的加入和移除仅发生在同一端——栈顶
#最新加入栈的数据项会先被移除 LIFO: Last in First out  后进先出
#一种基于数据项保存时间长度的结构，时间越短离栈顶越近（反转次序）
        
##### stack 抽象数据类型(ADT)  定义接口
        
class Stack: # push pop O(1)
    def __init__(self):
        self.item=[]
    def isEmpty(self):
        return self.item==[]
    def push(self,new):
        return self.item.append(new)
    def pop(self):
        return self.item.pop()
    def peek(self):
        return self.item[-1]
    def size(self):
        return len(self.item)
    
class Stack_reverse: # push pop O(n)
    def __init__(self):
        self.item=[]
    def isEmpty(self):
        return self.item==[]
    def push(self,new):
        return self.item.insert(0,new)
    def pop(self):
        return self.item.pop(0)
    def peek(self):
        return self.item[0]
    def size(self):
        return len(self.item)

s=Stack()
s=Stack_reverse()

s.isEmpty()
s.push(1)
s.push('dog')
s.peek()
s.size()
s.pop()
##############################
#   Check Bracket            #
##############################   
list='(()))'
def check_bracket(list):
    tmp=Stack()
    for element in list:
        if element=='(':
            tmp.push(element)
        else:
            if tmp.isEmpty():
                return False
            else:
                tmp.pop()
    if not list:
        return False
    return tmp.isEmpty()


def check_bracket_general1(list):
    dict={'[':']','(':')','{':'}'}
    tmp=Stack()
    for element in list:
        if element in dict:
            tmp.push(element)
        else:
            if tmp.isEmpty():
                return False
            else:
                top=tmp.pop()
                if dict[top]!=element:
                    return False
    if not list:
        return False
    return tmp.isEmpty()

check_bracket_general1(list)


def check_bracket_general2(list):
    tmp=Stack()
    for element in list:
        if element in '([{':
            tmp.push(element)
        else:
            if tmp.isEmpty():
                return False
            else:
                top=tmp.pop()
                if not match_bracket(top,element):
                    return False
    if not list:
        return False
    return tmp.isEmpty()
def match_bracket(a,b):
    list1='[{('
    list2=']})'
    return list1.index(a)==list2.index(b)

check_bracket_general2(list)
##############################
#   Decimal to binary        #
##############################                           
def divideby2(number):
    tmp=Stack() 
    integer=1
    while integer>0:
        remain=number%2
        tmp.push(remain)
        integer=number//2
        number=integer
    string=''    
    while not tmp.isEmpty():
        string=string+str(tmp.pop())
    return print(string)
    
divideby2(11232)
##############################
#   Decimal to Hexadecimal   #
##############################   

def divideby16(number):
    tmp=Stack() 
    integer=1
    digits='0123456789ABCDEF'
    while integer>0:
        remain=number%16
        remain=digits[remain]
        tmp.push(remain)
        integer=number//16
        number=integer
    string=''    
    while not tmp.isEmpty():
        string=string+str(tmp.pop())
    return print(string)
    
divideby16(11232)

##############################
#   Infix to postfix         #
##############################   
def infix_to_postfix(list):
    tmp=Stack()
    outputList=[]
    prec={}
    prec['*']=3
    prec['/']=3
    prec['+']=2
    prec['-']=2
    prec['(']=1
    list=list.split()
    for element in list:
        if element in 'abcdefghijklmnopqrstuvwxyz' or element in '0123456789':
            outputList.append(element)
        elif element=='(':
            tmp.push(element)
        elif element==')':
            out=tmp.pop()
            while out!='(':
                outputList.append(out)
                out=tmp.pop()
        else:
            while (not tmp.isEmpty()) and (prec[tmp.peek()]>=prec[element]):# first input of +
                outputList.append(tmp.pop())
            tmp.push(element)  
    #ouput:1232+
    #tmp:*+
    while not tmp.isEmpty():
        outputList.append(tmp.pop())
    return ' '.join(outputList)

list='1 + 2 * ( 3 + 2 ) '
infix_to_postfix(list)

list='1 2 3 2 + * +'
def postfixeval(list):
    list=list.split()
    tmp=Stack()

    for element in list:
        if element in '0123456789':
            tmp.push(element)
        else:
            b=tmp.pop()
            a=tmp.pop()
            result=calculate(int(a),int(b),element)
            tmp.push(result)
    return tmp.peek()
def calculate(num1,num2,special):
    if special=='+':
        return num1+num2
    elif special=='-':
        return num1-num2
    elif special=='*':
        return num1*num2
    else:
        return num1/num2
    
#Queue 队列：有次序的数据集合，一端进另一端出。数据进入（rear）尾端，另一端移除（front）
# first in first out(FIFO)
        
class Queue:
    def __init__(self):
        self.item=[]
    def isEmpty(self):
        return self.item==[]
    def enqueue(self,new): # O(n) 入列
        return self.item.insert(0,new)
    def dequeue(self): # O(1) 出列
        return self.item.pop()
    def size(self):
        return len(self.item)
    def peek(self):
        return self.item[-1]
def hotpotato(list,num):
    tmp=Queue()
    for name in list:
        tmp.enqueue(name)
    while tmp.size()>1:
        for _ in range(num):
            tmp.enqueue(tmp.dequeue())
        print(tmp.peek())
        tmp.dequeue()
    return print(tmp.dequeue())

hotpotato(['bob','sam','john','chan'],3)

import random
class Printer:
    def __init__(self,ppm):
        self.pagerate=ppm# 打印速度
        self.currentTask= None #打印任务
        self.timeRemaining=0 #任务倒计时
    def tick(self): #打印1秒
        if self.currentTask !=None:
            self.timeRemaining=self.timeRemaining-1 #经过一秒倒计时-1
            if self.timeRemaining<=0:   # 切换任务状态
                self.currentTask=None
    def busy(self):
        if self.currentTask != None:
            return True
        else:
            return False
    def startNext(self,newtask):
        self.currentTask = newtask
        self.timeRemaining=newtask.getPages()*60/self.pagerate
class Task:
    def __init__(self,time):
        self.timestamp = time
        self.pages = random.randrange(1,21)
    def getStamp(self):
        return self.timestamp
    def getPages(self):
        return self.pages
    def waitTime(self,currenttime):
        return currenttime-self.timestamp

def newPrintTask(): #生成新作业概率
    num = random.randrange(1,181)
    if num==180:
        return True
    else:
        return False


def simulation(numSeconds,pagesPerMinute):
    labprinter = Printer(pagesPerMinute)
    printQueue=Queue()
    waitingtimes= []
    
    for currentSecond in range(numSeconds): 
        if newPrintTask(): #若生成新任务
            task=Task(currentSecond) # 记录当前时刻 currentSecond以及随机生成打印页数
            printQueue.enqueue(task) #将新任务放入队列中
        if (not labprinter.busy()) and (not printQueue.isEmpty()): #printer not busy and queue not empty
            nexttask=printQueue.dequeue() # 打印机空闲将queue中的任务提出并print
            waitingtimes.append(nexttask.waitTime(currentSecond)) #  记录时间 
            labprinter.startNext(nexttask)
        labprinter.tick()
    averageWait=sum(waitingtimes)/len(waitingtimes)
    print("Average Wait %6.2f secs %3d tasks remaining."%(averageWait,printQueue.size()))
for i in range(10):
    simulation(3600,5)
    
    
    
    
    
## Deque 双端队列（有次序的数据集）
#既可以从队首也可以从队尾加入。
#数据可以从两端移除
    
class Deque:
    def __init__(self):
        self.item=[]
    def addFront(self,new):
        return self.item.append(new)
    def addRear(self,new):
        return self.item.insert(0,new)
    def size(self):
        return len(self.item)
    def removeRear(self):
        return self.item.pop(0)
    def removeFront(self):
        return self.item.pop()
    def isEmpty(self):
        return self.item==[]
    
def palchecker(strings):   # 回文词 radar
    if not strings:
        return False
    tmp=Deque()
    for element in strings:
        tmp.addFront(element)
    while 1:
        first=tmp.removeRear()
        last=tmp.removeFront()
        
        if tmp.size()>=1 and first!=last:
            return False
        if tmp.size()==0 or tmp.size()==1:
            return True
        
strings='radar'
palchecker(strings) 


#链表 存储不是按位置存放，通过链接指向即可保持前后相对位置 
#链表最先加入的元素位于链表的最后端，即越后面插入的数据，越接近与表头Head
class Node:
    def __init__(self,initdata):
        self.data=initdata
        self.next=None
    def getdata(self):
        return self.data
    def getNext(self):
        return self.next
    def setData(self,newdata):
        self.data=newdata
    def setNext(self,newnext):
        self.next=newnext

class UnorderedList:
    def __init__(self):
        self.head=None 
        self.dim=0
    def add(self,item):
        temp=Node(item)  # 初始化需要add的节点（赋值）生成节点1
        temp.setNext(self.head) #将该节点的下一节点连到head所指节点 连接节点1
        self.head=temp #将head连到新增的节点上
        self.dim+=1
    def isEmpty(self):
        if self.dim==0:
            return True 
        else:
            return False
    def size(self):
        current=self.head
        count=0
        while current !=None:
            count+=1
            current=current.getNext()
        return count
    def search(self,item):
        current=self.head
        found=False
        while current !=None and not found:
            if current.getdata()==item:
                found=True
                self.dim+=1
            else:
                current=current.getNext()
        return found
    
    def remove(self,item):
        current=self.head
        previous=None
        found=False
        while not found:
            if current.getdata()==item:
                found=True
            else:
                previous=current
                current=current.getNext()
        if previous== None:
            self.head=current.getNext()
        else:
            previous.setNext(current.getNext())
    def index(self,new): 
        current=self.head
        flag=False
        index=self.size()-1
        while not flag:
            if current.getdata()==new:
                flag=True    
            else:
                current=current.getNext()
                index-=1
        return index
    def pop(self,item=None):
        current=self.head
        flag=False
        if item == None:
            while 1:
                if current.getNext() is None:
                    output=current.getdata()
                    self.remove(current.getdata())
                    return output
                else:
                    current=current.getNext()

            
mylist=UnorderedList()
mylist.add(2)
mylist.add(3)
mylist.add(4)
mylist.size()
mylist.search(2)
mylist.remove(3)
mylist.isEmpty()
mylist.index(4)
mylist.pop(1)
#######
#OrderedList  有序表
class Node:
    def __init__(self,init):
        self.value=init
        self.next=None
    def getdata(self):
        return self.value
    def getnext(self):
        return self.next
    def setdata(self,new):
        self.value=new
    def setnext(self,new):
        self.next=new


class OrderedList:
    def __init__(self):
        self.head=None
    def add(self,new):
        current=self.head
        previous=None
        flag=False
        while not flag and current!=None:
            if current.getdata()>new:
                flag=True
            else:
                previous=current
                current=current.getnext()
        tmp=Node(new)
        if previous==None:
            tmp.setnext(self.head)
            self.head=tmp
        else:
            tmp.setnext(current)
            previous.setnext(tmp)
        
    def search(self,item):
        current=self.head
        flag=False
        stop=False
        while not flag and not stop and current !=None:
            if current.getdata()==item:
                flag=True
            else:
                current=current.getnext()
                if current.getdata()>item:
                    stop=True
        if flag==True:
            return True
        return False
        
    def isEmpty(self):
        if self.head is None:
            return True
        else:
            return False
        
mylist=UnorderedList()
mylist.add(2)
mylist.add(3)
mylist.add(4)
mylist.size()
mylist.search(2)
mylist.remove(3)
mylist.isEmpty()
mylist.index(4)
mylist.pop(1)
###递归
#将一个复杂问题分解为多个规模较小且较好解决的子问题
#1. 规模更小，调用自身
#2.最小规模，简单直接
def listsum(list):
    if len(list)==1:
        return list[0]
    else:
        return list[0]+listsum(list[1:])
listsum([1,2,3,23,4,12,54,24])


#进制
####递归返回刚好与栈相似
def tostr(number,base):
    symbol='0123456789ABCDEF'
    if number <base:
        return symbol[number]
    else:
        return tostr(number//base,base)+tostr(number%base,base)
tostr(12345,16)       
        
# 改变递归最大深度

import sys
sys.getrecursionlimit()
sys.setrecursionlimit(5000)
## 递归可视化

import turtle
t=turtle.Turtle() #生成turtle对象
t.forward(100)
turtle.done()

# square
t=turtle.Turtle()
for _ in range(4):
    t.forward(100)
    t.right(90)
turtle.done()

# star

import turtle
t=turtle.Turtle()
t.pencolor('red')
t.pensize(3)
for _ in range(5):
    t.forward(100)
    t.right(144)
t.hideturtle()
turtle.done()

#spiral
def drawspiral(t,length):
    if length>0:
        t.forward(length)
        t.right(90)
        drawspiral(t,length-2)
import turtle
t=turtle.Turtle()
drawspiral(t,100)    

# tree
def tree(length):
    if length>5:
        t.forward(length)
        t.right(30)
        tree(length-10)
        t.left(60)
        tree(length-10)
        t.right(30)
        t.backward(length)
        
import turtle
t=turtle.Turtle()
t.left(90)
t.pencolor('green')
t.pensize(3)
tree(75)

#sierpinski triangle
def sierpinski(degree,points):
    color=['blue','red','green','black','orange']
    drawtriangle(points,color[degree])#4
    if degree>0:
        sierpinski(degree-1,{'left':points['left'],'top':getmid(points['left'],points['top']),'right':getmid(points['right'],points['left'])})
        sierpinski(degree-1,{'left':getmid(points['left'],points['top']),'top':points['top'],'right':getmid(points['right'],points['top'])})
        sierpinski(degree-1,{'left':getmid(points['right'],points['left']),'top':getmid(points['right'],points['top']),'right':points['right']})

def getmid(point1,point2):
    return ((point1[0]+point2[0])/2,(point1[1]+point2[1])/2)
def drawtriangle(points,color):
    t.fillcolor(color)
    t.penup()
    t.goto(points['top'])
    t.pendown()
    t.begin_fill()
    t.goto(points['left'])
    t.goto(points['right'])
    t.goto(points['top'])
    t.end_fill()
t=turtle.Turtle()
points={'left':(-200,-100),
        'top':(0,200),
        'right':(200,-100)} 
sierpinski(4,points)

#hannoi
def hannoi(number,a,b,c):
    if number>0:
        hannoi(number-1,a,c,b)
        print('%s->%s'%(a,c))
        hannoi(number-1,b,a,c)
hannoi(3,'A','B','C')    
  
# maze
import turtle
mazeFileName='maze.txt'



class Maze(object):
	# 读取迷宫数据，初始化迷宫内部，并找到海龟初始位置。
	def __init__(self, mazeFileName):
		rowsInMaze = 0							#初始化迷宫行数
		columnsInMaze = 0 						#初始化迷宫列数
		self.mazelist = []						#初始化迷宫列表
		mazeFile = open(mazeFileName, 'r')		#读取迷宫文件
		for line in mazeFile:					#按行读取
			rowList = [] 						#初始化行列表
			col = 0 							#初始化列
			# for ch in line[:-1]:				#这样会丢失最后一列
			for ch in line:						#按列读取
				rowList.append(ch)				#添加到行列表
				if ch == 'S':					#S为乌龟初始位置，即迷宫起点
					self.startRow = rowsInMaze	#乌龟初始行
					self.startCol = col 		#乌龟初始列
				col = col + 1 					#下一列
			rowsInMaze = rowsInMaze + 1 		#下一行
			self.mazelist.append(rowList)		#行列表添加到迷宫列表
			columnsInMaze = len(rowList) 		#获取迷宫总列数
		self.rowsInMaze = rowsInMaze 			#设置迷宫总行数
		self.columnsInMaze = columnsInMaze		#设置迷宫总列数
		self.xTranslate = -columnsInMaze/2 		#设置迷宫左上角的初始x坐标
		self.yTranslate = rowsInMaze/2 			#设置迷宫左上角的初始y坐标
		self.t = turtle.Turtle()				#创建一个海龟对象
		self.t.shape('turtle')					#给当前指示点设置样式(类似鼠标箭头)，海龟形状为参数指定的形状名，指定的形状名应存在于TurtleScreen的shape字典中。多边形的形状初始时有以下几种："arrow", "turtle", "circle", "square", "triangle", "classic"。
		self.wn = turtle.Screen()				#创建一个能在里面作图的窗口
		self.wn.setworldcoordinates(-columnsInMaze/2, -rowsInMaze/2, columnsInMaze/2, rowsInMaze/2)			#设置世界坐标系，原点在迷宫正中心。参数依次为画布左下角x轴坐标、左下角y轴坐标、右上角x轴坐标、右上角y轴坐标

	# 在屏幕上绘制迷宫
	def drawMaze(self):
		self.t.speed(20)						#绘图速度
		for y in range(self.rowsInMaze):		#按单元格依次循环迷宫
			for x in range(self.columnsInMaze):
				if self.mazelist[y][x] == OBSTACLE:	#如果迷宫列表的该位置为障碍物，则画方块
					self.drawCenteredBox(x + self.xTranslate, -y + self.yTranslate, 'orange')

	# 画方块
	def drawCenteredBox(self, x, y, color):
		self.t.up()								#画笔抬起
		self.t.goto(x - 0.5, y - 0.5)			#前往参数位置，此处0.5偏移量的作用是使乌龟的探索路线在单元格的正中心位置
		self.t.color(color)						#方块边框为橙色
		self.t.fillcolor('green')				#方块内填充绿色
		self.t.setheading(90)					#设置海龟的朝向，标准模式：0 - 东，90 - 北，180 - 西，270 - 南。logo模式：0 - 北，90 - 东，180 - 南，270 - 西。
		self.t.down()							#画笔落下
		self.t.begin_fill()						#开始填充
		for i in range(4):						#画方块边框
			self.t.forward(1)					#前进1个单位
			self.t.right(90)					#右转90度
		self.t.end_fill()						#结束填充
	def moveTurtle(self, x, y):
		self.t.up()								#画笔抬起
		self.t.setheading(self.t.towards(x + self.xTranslate, -y + self.yTranslate))	#setheading()设置海龟朝向，towards()从海龟位置到由(x, y)，矢量或另一海龟位置连线的夹角。此数值依赖于海龟初始朝向，由"standard"、"world"或"logo" 模式设置所决定。
		self.t.goto(x + self.xTranslate, -y + self.yTranslate)	#前往目标位置

	# 画路径圆点
	def dropBreadcrumb(self, color):
		self.t.dot(color)						#dot(size=None, color)画路径圆点

	# 用以更新迷宫内的状态及在窗口中改变海龟位置，行列参数为乌龟的初始坐标。
	def updatePosition(self, row, col, val):
		self.mazelist[row][col] = val 			#设置该标记状态为当前单元格的值
		self.moveTurtle(col, row)				#移动海龟
		if val == PART_OF_PATH: 				#其中一条成功路径的圆点的颜色
			color = 'green'
		elif val == TRIED:						#尝试用的圆点的颜色
			color = 'black'
		elif val == DEAD_END:					#死胡同用的圆点的颜色
			color = 'red'
		self.dropBreadcrumb(color)				#画路径圆点并上色

	# 用以判断当前位置是否为出口。
	def isExit(self, row, col):
		return (row == 0 or row == self.rowsInMaze - 1 or col == 0 or col == self.columnsInMaze - 1)								#根据海龟位置是否在迷宫的4个边线位置判断

	# 返回键对应的值，影响searchFrom()中maze[startRow][startColumn]值的获取
	def __getitem__(self, key):
		return self.mazelist[key]

# 探索迷宫，注意此函数包括三个参数：一个迷宫对象、起始行、起始列。
def searchFrom(maze, startRow, startColumn):
	# 从初始位置开始尝试四个方向，直到找到出路。
	# 1. 遇到障碍
	if maze[startRow][startColumn] == OBSTACLE:
		return False
	# 2. 发现已经探索过的路径或死胡同
	if maze[startRow][startColumn] == TRIED or maze[startRow][startColumn]== DEAD_END:
		return False
	# 3. 发现出口
	if maze.isExit(startRow, startColumn):
		maze.updatePosition(startRow, startColumn, PART_OF_PATH)#显示出口位置，注释则不显示此点
		return True
	maze.updatePosition(startRow, startColumn, TRIED)#更新迷宫状态、设置海龟初始位置并开始尝试
	# 4. 依次尝试每个方向
	found = searchFrom(maze, startRow - 1, startColumn) or \
            searchFrom(maze, startRow + 1, startColumn) or \
            searchFrom(maze, startRow, startColumn - 1) or \
            searchFrom(maze, startRow, startColumn + 1)
	if found:													#找到出口
		maze.updatePosition(startRow, startColumn, PART_OF_PATH)#返回其中一条正确路径
	else:														#4个方向均是死胡同
		maze.updatePosition(startRow, startColumn, DEAD_END)
	return found



PART_OF_PATH = 'O'			#部分路径
TRIED = '.'					#尝试
OBSTACLE = '+'				#障碍
DEAD_END = '-'				#死胡同
myMaze = Maze('maze.txt')	#实例化迷宫类，maze文件是使用“+”字符作为墙壁围出空心正方形空间，并用字母“S”来表示起始位置的迷宫文本文件。
myMaze.drawMaze()			#在屏幕上绘制迷宫。
searchFrom(myMaze, myMaze.startRow, myMaze.startCol)	#探索迷宫


####贪心策略Greedy Method 
def get_change (total):
  #  25 10 1
    num1=0
    num2=0
    num3=0
    while 1:
        if total>=25:
            num1+=1
            total=total-25    
        else:
            if total>=10:
                num2+=1
                total-=10
            else:
                num3=total
                total=total-num3
        if total==0:
            break
    print('$25: ',num1,'$10: ',num2,'$1: ',num3)  
get_change(63)


def moneychange(list,total):
    count=0
    while 1:
        if list:
            max_value=max(list)
            while total>=max_value:
                count+=1
                total-=max_value
            list.remove(max_value)
        else:
            return count
moneychange([25,10,1],63)

#当币种组合出现21时，改方法失效

###递归解法 尝试每个币种，递归调用得到硬币数，比较求四种尝试种最小的数量
import time 
t1=time.time()
def recMC(list,total):
    min=total
    if total in list:
        return 1
    for i in [c for c in list if c <total]:
        num=recMC(list,total-i)+1
        if num<min:
            min=num
    return min
recMC([1,5,10,25],63)
t2=time.time()
print(t2-t1)
#低效,重复计算过多


###存储中间表的递归

def recMC_store(list,total,knownresults):
    min=total
    if total in list:      #若剩余金额满足币种，直接返回个数1并记录
        knownresults[total]=1
        return 1
    elif knownresults[total]>0: #若存储值大于0，改情况已经计算过直接查表输出
        return knownresults[total]
    else:  
        for i in [c for c in list if c<total]: #for 循环中，即在所有四种情况中寻找最小的数量，并返回存储min 
            num=recMC_store(list,total-i,knownresults)+1 #继续递归，并个数+1
            if num<min:  #四种情况的最小值 (1+numcoins(total-1)) ,1+numcoins(total-5),1+numcoins(total-10),1+numcoins(total-25)
                min=num
                knownresults[total]=min
    return min
recMC_store([1,5,10,25],63,[0]*64)  


#####动态规划
#递归算法会重复计算，使用存储可以解决重复计算，但该方法不能称为动态规划
#只能认为是memoization 记忆化/函数值缓存

#动态规划
####关键：该类问题依赖于更少数问题的最优解，而更少数问题的最优解已经得到。
#####大问题的最优解包含了更小规模子问题的最优解。（必要条件）            
###找出问题的转移状态方程，以及定义list去存储每一步的最优值
def dpmakechange(list,total,storage,coinused):
    #  从1分开始逐个计算最少的硬币数
    for cents in range(1,total+1):
        #初始化一个最大值
        coincount=cents
        newcoin=1
        #减去每个硬币，向后查找最少硬币数并记录最少
        for j in [c for c in list if c<=cents]:  # 对于小于当前最大值的所有情况进行循环并求min 
            if storage[cents-j]+1<coincount:
                coincount=storage[cents-j]+1
                newcoin=j
        coinused[cents]=newcoin
        #得到最少的硬币数并存储
        storage[cents]=coincount
    return storage[total],coinused
def printcoins(coinused,change):
    coin=change
    while coin>0:
        thiscoin=coinused[coin]
        print(thiscoin)
        coin=coin-thiscoin

a,coinused=dpmakechange([1,3,5,25],63,64*[0],64*[0])
printcoins(coinused,63)




###博物馆大盗
### object   1.  2. 3. 4. 5.
### weight   2   3  4  5  9
### value    3   4  8  8  10



#####绘制二维列表


####若将[0]*21改为一个变量.e.g. x=[0]*21  append(x)所有行都同时改变
tmp=[]
for _ in range(6):
    tmp.append([0]*21)
dict=[0,{'w':2,'v':3},{'w':3,'v':4},{'w':4,'v':8},{'w':5,'v':8},{'w':9,'v':10}]

for i in range(1,6):
    for j in range(1,21):
        if dict[i]['w']>j:
            tmp[i][j]=tmp[i-1][j]
        else:
            tmp[i][j]=max(tmp[i-1][j],tmp[i-1][j-dict[i]['w']]+dict[i]['v'])
print(tmp[5][20])
            

##################################################################################

tr=[None,{'w':2,'v':3},{'w':3,'v':4},{'w':4,'v':8},{'w':5,'v':8},{'w':9,'v':10}] 

max_w=20

m={(i,w):0 for i in range(len(tr)) for w in range(max_w+1)}#多个dict组成的list

for i in range(1,len(tr)):
    for w in range(1,max_w+1):
        if tr[i]['w']>w:# 物品的weight>第w列
            m[(i,w)]=m[(i-1,w)]
        else:
            m[(i,w)]=max(m[(i-1,w)],tr[i]['v']+m[(i-1,w-tr[i]['w'])])
print(m[(5,20)])
            
###################################################################################
#递归

dict={(2,3),(3,4),(4,8),(5,8),(9,10)} #set
max_w=20
m={} #构建字典
def thief(dict,w):
    if dict==set() or w==0:
        m[(tuple(dict),w)]=0
        return 0
    elif (tuple(dict),w)in m:
        return m[(tuple(dict),w)]
    else:
        vmax=0
        for t in dict:
            if t[0]<=w:
                v=thief(dict-{t},w-t[0])+t[1]
                vmax=max(vmax,v)
        m[(tuple(dict),w)]=vmax
        return vmax
print(thief(dict,max_w))

def queen(A, cur=0):
    if cur == len(A):  #停止条件
        print(A)
        return 0
    for col in range(len(A)):
        A[cur], flag = col, True #第cur行放在第col列上 0-7
        for row in range(cur):
            if A[row] == col or abs(col - A[row]) == cur - row:
                flag = False
                break #跳出该for循环，回溯到上一层解决该问题
        if flag:
            queen(A, cur+1)
queen([None]*8)


### object   1.  2. 3. 4. 5.
### weight   2   3  4  5  9
### value    3   4  8  8  10

#递归          
dict={(2,3),(3,4),(4,8),(5,8),(9,10)} #set
max_w=20
m={} #构建字典
def thief(dict,w):
    if dict==set() or w==0:
        m[(tuple(dict),w)]=0
        return 0
    elif (tuple(dict),w)in m:
        return m[(tuple(dict),w)]
    else:
        vmax=0
        for t in dict:
            if t[0]<=w:
                v=thief(dict-{t},w-t[0])+t[1]
                vmax=max(vmax,v)
        m[(tuple(dict),w)]=vmax
        return vmax
print(thief(dict,max_w))

    
limit=20
dict={(2,3),(3,4),(4,8),(5,8),(9,10)}
m={}
def theft_rec(dict,limit):
    if  dict==set() or limit==0  :
        m[(tuple(dict),limit)]=0
        return 0 
    elif (tuple(dict),limit) in m:
        return m[(tuple(dict),limit)]
    else:
        best=0
        for i in dict:
            if i[0]<=limit:
               result=theft_rec(dict-{i},limit-i[0])+i[1]
               best=max(result,best)
        m[(tuple(dict),limit)]=best
        return best
print(theft_rec(dict,limit) )
########顺序查找  Sequential Search
def sequentailSearch(List,target):
    flag=False
    index=0
    while index<len(List) and not flag:
        if List[index]==target:
            return True
        else:
            index+=1
    return flag
sequentailSearch([1,23,34,1,24,124,1242],1242)

def ordersenquentialsearch(List,target):
    flag= False
    stop= False
    index=0 
    while not flag and not stop and index<len(List):
        if List[index]==target:
            return True
        else:
            if List[index]>target:
                return False,index
            index+=1
    return False
ordersenquentialsearch([1,3,5,77,124,252,46436],34)

######################二分查找——分治策略：每次缩小问题规模，将结果汇总到原问题的解
def binarysearch(list,target):
    left=0
    right=len(list)-1
    while left<=right:
        
        tmp=(left+right)//2
        if list[tmp]==target:
            return True
        else:
            if list[tmp]<target:
                left=tmp+1
            else:
                right=tmp-1
    return False

binarysearch([1,2,3,5,7,8,99],3)

def binarysearch_recur(list,target):
    if len(list)==0:
        return False
    else:
        tmp=len(list)//2
        if list[tmp]==target:
            return True
        elif list[tmp]<target:
            result=binarysearch_recur(list[tmp+1:],target)# 切片的复杂度为O(n)，故可以通过tmp来代替切片
        else:
            result=binarysearch_recur(list[:tmp],target)
    return result
binarysearch_recur([1,2,3,5,7,8,99],99)


####具体选择什么算法需依赖于实际应用情况

###########冒泡排序
###需要多次对比，其中大部分操作是无效的，但不需要额外存储空间
def bubblesort(list):
    for i in range(len(list)-1,0,-1):
        for j in range(i):
            if list[j]>list[j+1]:
                list[j],list[j+1]=list[j+1],list[j]
    return list
bubblesort([1,4,2,6,73,4,356,34,2,235,234,6,4])

##优化冒泡排序
#若一次扫描下来，没有元素进行改变，则后续排序无需进行
# O(N^2)
def bubblesort_optimize(list):
    flag=True
    index=len(list)-1
    while index>0 and flag:
        flag=False
        for j in range(index):
            if list[j]>list[j+1]:
                list[j],list[j+1]=list[j+1],list[j]
                flag=True
        index-=1
    return list
bubblesort_optimize([1,4,2,6,73,4,356,34,2,235,234,6,4])                
            
####选择排序 （基于冒泡排序）但只是记录每一趟的最大值，并最后进行交换。
#稍微优于冒泡排序 
#O(N^2)
def selectsort(list):
    index=len(list)-1  
    while index>0:
        max_index=0
        for i in range(0,index+1):###这里需取到所有element
            if list[i]>list[max_index]:
                max_index=i
        list[index],list[max_index]=list[max_index],list[index]
        index-=1
    return list
selectsort([1,4,2,6,73,4,356,34,2,235,234,6,4])   

##插入排序 视为两个部分，1.已经排序好的子列，
#移动只有一次赋值，所以性能较好 
#O(n^2) 
#最好情况O（n）,越接近有序，插入排序比对次数越小
def insert_sort(list):
    for i in range(1,len(list)):
        value=list[i]
        position= i
        while position >0 and list[position-1]>value:
            list[position]=list[position-1]
            position=position-1
        list[position]=value
    return list
insert_sort([1,4,2,6,73,4,356,34,2,235,234,6,4])      


#shell sort 以插入排序作为基础，对无序表进行间隔划分出子列表，在每个子列表用插入排序 
#以不同间隔对列表进行排序。n/2,n/4,8/n,1
# O(n)到O(n^2)之间
#如果间隔(2^k)-1,则O(n^2/3)
##但极端情况，可能等于O(n^2)或者更大，等比间隔会形成盲区 # 2 1 5 3 7 6 9 8 
#希尔排序不稳定，相同的值可能会发生调换
   

def shell(lis):
    n = len(lis)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            while i >= gap and lis[i] < lis[i - gap]:
                lis[i], lis[i - gap] = lis[i - gap], lis[i]
                i -= gap
        gap //= 2
    return lis 
shell([1,4,2,6,73,4,356,34,2,235,234,6,4])  

def shell(list):
    n=len(list)
    gap=n//2
    while gap>0:
        for i in range(gap,n):
            index=i
            value=list[i]
            while index>0 and value<list[index-gap]:
                list[index]=list[index-gap]
                index-=gap
            list[index]=value
        gap=gap//2
    return list


#归并排序 MergeSort
#采用分治策略，递归
    
####分裂和归并
    #分裂过程：O(logn)
    #归并过程：O(n)
    #合计O(nlogn)
    #用了存储空间，若数据量很大则不好执行
def mergesort(list):
    if len(list)<=1:
        return list
    middle=len(list)//2
    left=mergesort(list[:middle])
    right=mergesort(list[middle:])
    
    new=[]
    while left and right:
        if left[0] <=right[0]:
            new.append(left.pop(0))
        else:
            new.append(right.pop(0))
    new.extend(right if right else left )
    return new

mergesort([1,4,2,6,73,4,356,34,2,235,234,6,4])




#####快速排序
#选第一个元素为初始中值，设立两个游标，left,right， left一值向右如果遇到比中值大的停下来
#right一直向左，直到遇到一个比中值小的停下来
#交换left和right
#根据一个中值，将数据分为两半：小于中值的一半与大于中值的一半，然后对每一个部分进行快排（递归）
#O(nlogn)
####极端情况，中值选取太偏倚，且划分的两个子列中某一个元素过少，时间复杂度 为O(n^2)甚至更大， 不如冒泡
#不用额外存储
def quick_sort(array, start, end):
    if start >= end:
        return
    left =start 
    right = end
    key = array[start]
    while left < right:
        while left < right and array[right] > key:   ###挖坑填数
            right -= 1
        array[left] = array[right]
        while left < right and array[left] <= key:
            left += 1
        array[right] = array[left]
    #退出循环 left right相等
    array[left] = key
    quick_sort(array, start, left - 1)
    quick_sort(array, left + 1, end)
    return array
quick_sort([1,4,2,6,73,4,356,34,2,235,234,6,4],0,len([1,4,2,6,73,4,356,34,2,235,234,6,4])-1)



#####散列Hashing  查找
#增加更多先验知识即事先知道数据项应该出现于什么位置O(1)

#散列函数:实现从数据项到存储槽转换 e.g. %求余数
# 称 被数据项占据的槽slot为负载因子  6 out of 11 =6/11
#查询只需用相同的散列函数映射，得到的结果于散列表对应的上则查到，但是会有冲突‘collision’ 66%11 与 77%11 冲突

#完美散列函数：如果一个散列函数能把所有数据项映射到不同的槽中
#寻找近似散列函数，冲突最少，计算难度低，充分分散数据项
#MD5 SHA

import hashlib


m=hashlib.md5()
m.update(b'Chen Hu')
m.hexdigest()
hashlib.sha256(b'Chen Hu').hexdigest()

#散列函数设计
#1.折叠法：将数据按位数分为若干段，求和，求余数 （隔数反转  1 73（37） 2 56（65））
#2.平方取中，44*44=1936，93%11=5(计算量稍大)
#3.非数项，转换为ASCII码  ord('A')
(ord('A')+ord('B')+ord('C'))%11
def hash(string,tablesize):
    sum=0
    for i in string :
        sum+=ord(i)
    return sum%tablesize

hash('ABC',11)

#对于变位词可考虑权重

#设计太复杂，使hash table失去意义，不如直接排序查找



############解决冲突
#open addressing 开放定址
#线性探测，从冲突槽开始向后扫描，寻找空值，若到末尾回到开头（linear probing）
###########缺点：会有聚集，过多数据等于1，则会占据1后的几个槽造成其他的新插入一直顺延
#跳跃探测：不是线性找下一个，而是加一个定值，e.g.+3  解决聚集 skip不能被散列表整除，故可以将散列表长度设置为质数prime
#二次探测 quadratic probing, skip= 1 3 5 7 9,  1 4 9 16
#####
#可抽象出来为rehashing再散列，rehash(pos)=(pos+skip)%sizetable


#数据项链  ，每个槽可以append冲突的值，折中进行线性查抄

#python 内置dictionary 查找O(1)

#ADT map
class Hashtable:
    def __init__(self):
        self.size=11
        self.slots=[None]*self.size
        self.data=[None]*self.size
    def hashfunction(self,key):
        return  key%self.size
    def rehash(self,oldhash):
        return (oldhash+1)%self.size
    def put(self,key,data):
        hashvalue=self.hashfunction(key)
        if self.slots[hashvalue ] ==None:
            self.slots[hashvalue]=key
            self.data[hashvalue]=data
        else:
            if self.slots[hashvalue]==key:# 相同的key但是value不同，则进行替换
                self.data[hashvalue]=data
            else:
                nextslots=self.rehash(hashvalue)
                while self.slots[nextslots]!=None and self.slots[nextslots]!=key:
                    nextslots=self.rehash(nextslots)
                if self.slots[nextslots]==None:
                    self.slots[nextslots]=key
                    self.data[nextslots]=data
                else:
                    self.data[nextslots]=data
    def gets(self,key):
        startslots=self.hashfunction(key)#用相同的function映射
        found=False
        stop=False
        position=startslots
        data=None
        while self.slots[position]!=None and not found and not stop:
            if self.slots[position]==key:
                found =True
                data=self.data[position]
            else:
                position=self.rehash(position)
                if position==startslots:
                    stop=True
        return data
    def __getitem__(self,key):
        return self.gets(key)
    def __setitem__(self,key,data):
        self.put(key,data)
h=Hashtable()
h[54]='cat'        
h[26]='dog'
h[93]='lion'
h[17]='tiger'
h[77]='bird'
h[31]='cow'
h[44]='goat'
h[55]='pig'
h[20]='chicken'
print(h.slots)    
print(h.data)
print(h[20])
print(h[17])
h[20]='duck'
print(h[20])
   
###############树
#根节点：树结构的最上端没有入边
#叶节点：树结构的最下端没有出边
#路径：由边依次连接在一起的节点构成的有序列表
#兄弟节点：共有一个父节点，且位于同一层
#层级level:由根节点开始到达叶节点的路径所包含的边的数量，成为层级。根节点层级为0
#高度：树中所有节点的最大层数，0，1，2



#list实现二叉树
def binary_tree(r):
    return [r,[],[]]
def insertLeft(root,newbranch):
    t=root.pop(1)
    if len(t)>1:
        root.insert(1,[newbranch,t,[]])
    else:
        root.insert(1,[newbranch,[],[]])
    return root

def insertRight(root,newbranch):
    t=root.pop(2)
    if len(t)>1:
        root.insert(2,[newbranch,[],t])
    else:
        root.insert(2,[newbranch,[],[]])
    return root
def getRootvalue(root):
    return root[0]
def setRootvalue(root,new):
    root[0]=new
def getleftchild(root):
    return root[1]
def getrightchild(root):
    return root[2]

r=binary_tree(3)
insertLeft(r,4)
insertLeft(r,5)
insertRight(r,6)
insertRight(r,7)
l=getleftchild(r)
print(l)
setRootvalue(l,9)
print(r)
insertLeft(l,11)
print(r)
print(getrightchild(getrightchild(r)))
class tree:#未使用递归，故只能保留根节点
    def __init__(self,val):
        self.root=[val,[],[]]
    def insertLeft(self,newbranch):
        t=self.root.pop(1)
        if len(self.root)>1:
            return self.root.insert(1,[newbranch,t,[]])
        else:
            self.root.insert(1,[newbranch,[],[]])
        return self.root

    def insertRight(self,newbranch):
        t=self.root.pop(2)
        if len(t)>1:
            self.root.insert(2,[newbranch,[],t])
        else:
            self.root.insert(2,[newbranch,[],[]])
        return self.root
    def getRootvalue(self):
        return self.root[0]
    def setRootvalue(self,new):
        self.root[0]=new
    def getleftchild(self):
        return self.root[1]
    def getrightchild(self):
        return self.root[2]
    

t=tree(0)
t.insertLeft(4)
t.insertLeft(5)
t.insertRight(6)
t.insertRight(7)
l=t.getleftchild()
print(l)


class binaryTree:
    def __init__(self,root):
        self.key=root
        self.left=None
        self.right=None
            
    def insert_left(self,newNode):
        if self.left==None:
            self.left=binaryTree(newNode)
        else:
            tmp=binaryTree(newNode)
            tmp.left=self.left
            self.left=tmp
    def insert_right(self,newNode):
        if self.right==None:
            self.right=binaryTree(newNode)
        else:
            tmp=binaryTree(newNode)
            tmp.right=self.right
            self.right=tmp
    def getrightchild(self):
        return self.right
    def getleftchild(self):
        return self.left
    def setrootval(self,value):
        self.key=value
    def getrootval(self):
        return self.key
r=binaryTree('a')
r.insert_left('b')
r.insert_right('c')
r.getrightchild().setrootval('hello')
r.getleftchild().insert_right('d')
        
######
#将树用表示于语言中的句子，可以分析句子中的各种语法成分。nlp
#表达解析式，用叶节点保存操作数，内部节点保存操作符
#越靠近叶节点，优先级越高
class Stack: # push pop O(1)
    def __init__(self):
        self.item=[]
    def isEmpty(self):
        return self.item==[]
    def push(self,new):
        return self.item.append(new)
    def pop(self):
        return self.item.pop()
    def peek(self):
        return self.item[-1]
    def size(self):
        return len(self.item)
    
def buildparseTree(fpexp):
    fplist=fpexp.split()
    pstack=Stack()
    etree=binaryTree('')
    pstack.push(etree)
    currenttree=etree
    for i in fplist:
        if i =='(':
            currenttree.insert_left('')
            pstack.push(currenttree)
            currenttree=currenttree.getleftchild()
        elif i not in ['+','-','*','/',')']:
            currenttree.setrootval(int(i))
            parent=pstack.pop()
            currenttree=parent
        elif  i in ['+','-','*','/'] :
            currenttree.setrootval(i)
            currenttree.insert_right('')
            pstack.push(currenttree)
            currenttree=currenttree.getrightchild()
        elif  i==')':
            currenttree=pstack.pop()
        else:
            raise ValueError
    return etree
#求值
import operator
def evaluate(parsetree):
    opers={'+':operator.add,'-':operator.sub,'*':operator.mul,'/':operator.truediv}
    leftC=parsetree.getleftchild()
    rightC=parsetree.getrightchild()
    
    if leftC and rightC:
        fn=opers[parsetree.getrootval()]
        return fn(evaluate(leftC),evaluate(rightC))
    else:
        return parsetree.getrootval()
fpexp='( ( 7 + 3 ) * ( 5 - 2 ) )'           
a= buildparseTree(fpexp)
evaluate(a)
def postordereval(tree):
    opers={'+':operator.add,'-':operator.sub,'*':operator.mul,'/':operator.truediv}
    va1=None
    va2=None
    if tree:
        va1=postordereval(tree.getleftchild())
        va2=postordereval(tree.getrightchild())
        if va1 and va2:
            return opers[tree.getrootval()](va1,va2)
        else:
            return tree.getrootval()
postordereval(a)

def printinorder(tree):
    out=''
    if tree:
        if tree.getrootval() in [0,1,2,3,4,5,6,7,8,9]:
            out=printinorder(tree.getleftchild())
        else:
            out='('+printinorder(tree.getleftchild())
            
        out=out+str(tree.getrootval())
        if tree.getrootval() in [0,1,2,3,4,5,6,7,8,9]:
            out=out+printinorder(tree.getrightchild())
        else:
            out=out+printinorder(tree.getrightchild())+')'
    return out
printinorder(a)
#####树的遍历（非线性结构）
#1.前序遍历preorder: 先访问根节点，再递归的前序访问左子树，最后访问右子树：与看书顺序类似
#2.中序遍历inorder:先递归的中序访问左子树，在访问根节点，再中序访问右子树
#3.后续遍历postorder:先递归的后续访问左子树，再访问右子树，最后访问根节点

def preorder(tree):
    if tree:
        print(tree.getrootval())
        preorder(tree.getleftchild())
        preorder(tree.getrightchild())
preorder(a)

def inorder(tree):
    if tree:
        preorder(tree.getleftchild())
        print(tree.getrootval())
        preorder(tree.getrightchild())
inorder(a)

def postorder(tree):
    if tree:
        preorder(tree.getleftchild())
        preorder(tree.getrightchild())
        print(tree.getrootval())
postorder(a)


####优先队列 Priority Queue(VIP)
#高优先级的数据项排在队首，低优先级往后排
#出队都是以队首先出
#二叉堆（Binary Heap）:保持入队出队复杂度都是O(logN)
#逻辑结构像二叉树，但其实使用非嵌套的列表实现
#最小的key(优先级最高的)放于队首，min heap

#对数水平：二叉树  始终保持在对数水平：平衡二叉树（树根左右子树拥有的相同数量的节点）
#第k层：个数2^k-1
#完全二叉树来近似平衡二叉树

####完全二叉树：叶节点最多只出现再底层和次底层，而且最底层的叶节点都连续集中在最左边，
#每个内部节点都有两个子节点，最多可有一个节点例外。
#从1计为根节点，则一个节点下表为p，左子节点2P,右子节点2P+1,父节点P//2

##堆次序：Heap order
#任何一个节点，其父节点的key小于x中的key(根节点key最小)（部分有序）

class biheap:
    def __init__(self):
        self.heaplist=[0]#保留index=0
        self.currentsize=0
    def insert(self,new):#插入到最下层的最右端，但是会破坏堆次序，故对该路径进行上浮，不影响其他路径的次序
        self.heaplist.append(new)
        self.currentsize+=1
        self.percUp(self.currentsize)
    def percUp(self,i):
        flag=False
        while i>0 and not flag:
            if self.heaplist[i]<self.heaplist[i//2]:
                flag=True#上一层没有改变则停止
                self.heaplist[i],self.heaplist[i//2]=self.heaplist[i//2], self.heaplist[i]
            i=i//2
    def delMin(self):  #pop出根节点（最小的key）,选择最下一层最右边的值进行替换root，当需要下沉直到比所有的子节点都小,选择较小的子节点进行下沉
        retri=self.heaplist[1]
        self.heaplist[1]=self.heaplist[self.currentsize]
        self.currentsize=self.currentsize-1
        self.heaplist.pop()
        self.percDown(1)
        return retri
    def percDown(self,i):
        while i*2<=self.currentsize:
            new=self.minchild(i)
            if self.heaplist[i]>self.heaplist[new]:
                self.heaplist[i],self.heaplist[new]=self.heaplist[new],self.heaplist[i]
            i=new
    def minchild(self,i):
        if i*2+1>self.currentsize:
            return i*2
        else:
            if self.heaplist[i*2]>self.heaplist[2*i+1]:
                return 2*i+1
            else:
                return 2*i
    def buildHeap(self,list): #若逐个insert入堆中，时间复杂度O(NlogN),下沉法O(logN))，直接将list视为一个堆，则只需对父节点进行下沉
        i=len(list)//2   #最后一个父节点
        self.currentsize=len(list) #有0
        self.heaplist=[0]+list[:]
        print(len(self.heaplist),i)
        while i>0:
            print(self.heaplist,i)            
            self.percDown(i)
            i-=1
        print(self.heaplist,i)
bn=biheap()
bn.insert(5)
bn.insert(7)
bn.insert(3)
bn.insert(11)
print(bn.delMin())
bn.buildHeap([3,2,4,6,3,1,2,7,8,6,3,])





