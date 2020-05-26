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
        




