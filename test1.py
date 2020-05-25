import random

aim = '123456789'
w = random.choice(aim)   #猴子的位置
x = 0                    #猴子否爬上仙子
y = random.choice(aim)   #箱子的位置
z = 0                    #猴子是否摘到香蕉
i = 0                    #计算总的状态数
end = random.choice(aim) #香蕉的位置

def Go(temp):                       #猴子空手走
    global w
    global i
    if w != temp:
        i = i + 1
        w = temp
        print("第%d步：" %i)
        print((w,x,y,z))

def GoWithBox(temp):                 #猴子推箱子
    global w
    global y
    global i
    if w == y:
        if y != temp:
            i = i + 1
            y = temp
            w = temp
            print("第%d步：" % i)
            print((w,x,y,z))
    else:
        print("error");

def OnBox():                         #猴子爬箱子
    global x
    global i
    i = i + 1
    x = 1
    print("第%d步：" % i)
    print((w,x,y,z))

def GetBan():                        #猴子宅现浇
    global z
    global i
    if w == y and x == 1:
        z = 1
        i = i + 1
        print("地%d步.    猴子成功摘到香蕉:" % i)
        print((w, x, y, z))
    else:
        print('摘不到香蕉')

def Jump():
    global x
    global i
    x = 0
    i = i + 1
    print("第%d步：" % i)
    print((w,x,y,z))

if __name__ == '__main__':
    while (z==0):
        step = random.choice(aim)
        if (w < y and step < y) or (w > y and step > y):  # 找不到箱子的情况
            Go(step)
            continue
        else:                                         # 找到箱子
            Go(y)

        if (random.randint(0, 1)  == 0):        #决定猴子是否爬上箱子
            OnBox()
            if (y != end):                      #如果没有香蕉，就跳下箱子
                Jump()
                continue
            else:                               #有香蕉就摘香蕉
                GetBan()
                break
        else:
            GoWithBox(random.choice(aim))       #不上箱子就推着箱子走
            continue