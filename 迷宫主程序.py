'''
    作业说明
        请补全?处缺失的代码(可参考3.py对应注释的代码)

        需要录制视频，尝试讲解过程，最后别忘了朗读本节课学到的词汇哦（中英文各2遍）~
'''
#导入模块
import pygame
import mazeData
import random
import ybc_box as box
import sys

#初始化pygame并更改名字
pygame.init()
screen = pygame.display.set_mode([1330, 690])
pygame.display.set_caption('迷宫挑战')

#初始化字体
text = pygame.font.SysFont("C:\Windows\Fonts\STZHONGS.TTF", 60)

#更改游戏图标
surface =  pygame.image.load('image\maze.jpg').convert_alpha()
pygame.display.set_icon(surface)

#初始化变量
x = 30
y = 30
long = 360
dead_y2 = 260
dead_y1 = 480
dead_x = 0
brave = 1
brave_time = -100000
step = 0
time = 10000
dead_time = 0

# 生成迷宫地图
maze = mazeData.Maze()

#设置闹钟
clock = pygame.time.Clock()

#主循环
while True:
    # 使用for循环遍历当前事件列表
    for event in pygame.event.get():
        # 判断【事件类型】是不是【按下键盘事件】
        if event.type == pygame.KEYDOWN:
            # 判断【事件按键】是不是【上移键】
            if event.key == pygame.K_UP:
                color = screen.get_at([x, y - 30])
                if color[0] == 255 and color[1] == 255 and color[2] == 255:
                    y = y - 30
                    step += 1
                elif brave == 1:
                    if color[0] == 254:
                        y = y - 30
                        box.msgbox('你已死亡\n\n原因:触摸岩浆')
                        x = 30
                        y = 30
                        brave = 0
                        brave_time = 1
                        dead_time += 1
                        if dead_time % 2 == 0:
                            maze = mazeData.Maze()
            # 判断【事件按键】是不是【下移键】
            elif event.key == pygame.K_DOWN:
                color = screen.get_at([x,y + 30])
                if color[0] == 255 and color[1] == 255 and color[2] == 255:
                    y = y + 30
                    step += 1
                elif brave == 1:
                    if color[0] == 254:
                        y = y + 30
                        box.msgbox('你已死亡\n\n原因:触摸岩浆')
                        x = 30
                        y = 30
                        brave = 0
                        brave_time = 1
                        dead_time += 1
                        if dead_time % 2 == 0:
                            maze = mazeData.Maze()
            # 判断【事件按键】是不是【左移键】
            elif event.key == pygame.K_LEFT:
                color = screen.get_at([x - 30,y])
                if color[0] == 255 and color[1] == 255 and color[2] == 255:
                    x = x - 30
                    step += 1
                elif brave == 1:
                    if color[0] == 254:
                        x = x - 30
                        box.msgbox('你已死亡\n\n原因:触摸岩浆')
                        x = 30
                        y = 30
                        brave = 0
                        brave_time = 1
                        dead_time += 1
                        if dead_time % 2 == 0:
                            maze = mazeData.Maze()
            # 判断【事件按键】是不是【右移键】
            elif event.key == pygame.K_RIGHT:
                color = screen.get_at([x + 30,y])
                if color[0] == 255 and color[1] == 255 and color[2] == 255:
                    x = x + 30
                    step += 1
                elif brave == 1:
                    if color[0] == 254:
                        x = x + 30
                        box.msgbox('你已死亡\n\n原因:触摸岩浆')
                        x = 30
                        y = 30
                        brave = 0
                        brave_time = 1
                        dead_time += 1
                        if dead_time % 2 == 0:
                            maze = mazeData.Maze()
        if event.type == pygame.QUIT:
            sys.exit()
    # 填充背景色
    screen.fill([161, 207, 143])

    # 绘制迷宫
    maze.draw(screen)
    
    #绘制岩浆河
    if not long > 1290:
        long += 4
    else:
        long = 0
        dead_y1 = random.randint(0,1000)
        dead_y2 = random.randint(0,1000)
        
    pygame.draw.rect(screen, [254, 0, 0], [0, dead_y1, long, 50])
    pygame.draw.rect(screen, [254, 0, 0], [0, dead_y2, long, 50])
    pygame.draw.rect(screen, [254, 0, 0], [dead_y2, 0, 50, long])
    pygame.draw.rect(screen, [254, 0, 0], [dead_y1, 0, 50, long])

    # 绘制方块
    if brave == 0:
        pygame.draw.rect(screen, [0, 0, 0], [x, y, 30, 30])
    else:
        pygame.draw.rect(screen, [237, 112, 129], [x, y, 30, 30])
    
    #减少时间
    time -= 1
    #绘制字体
    now = str(time/100)
    words = text.render(now, 1, (230, 230, 230))
    screen.blit(words,(1200, 20))
    
    #检擦触碰岩浆
    try:
        color1 = screen.get_at([x - 1,y - 1])
    except IndexError:
        color1 = [None]
    
    try:
        color2 = screen.get_at([x + 31,y + 31])
    except IndexError:
        color2 = [None]
    
    try:
        color3 = screen.get_at([x - 1,y + 31])
    except IndexError:
        color3 = [None]
    
    try:
        color4 = screen.get_at([x + 31,y - 1])
    except IndexError:
        color4 = [None]
        
    if color1[0]==254 or color2[0]==254 or color3[0]==254 or color4[0]==254:
        if brave == 1:
            box.msgbox('你已死亡\n\n原因:触摸岩浆')
            x = 30
            y = 30
            brave = 0
            brave_time = 1
            dead_time += 1
            if dead_time % 2 == 0:
                maze = mazeData.Maze()
    
    #无敌时间计时⏲
    if brave_time == 500:
        brave_time = -100000
        brave = 1
    elif brave_time > -52222:
        brave_time += 1
     
    #检查是否到达终点
    if x == 1200 and y == 630:
        f = open('best_step.txt','r')
        best_step = f.read()
        f.close()
        if step < int(best_step):
            box.msgbox('恭喜你突破了最高纪录' + '\n你的记录:' + str(step)  +'\n最高纪录:' + str(best_step))
            f = open('best_step.txt','w')
            f.write(str(step))
            f.close()
            brave_time = -900
        elif step > int(best_step):
            box.msgbox('恭喜你用了' + str(step) + '步来通关\n距离最高纪录还差' + str(step - int(best_step)))
            brave_time = -90
        elif step == int(best_step):
            box.msgbox('恭喜你用了' + str(step) + '\n你再少走一步就可以超过最高记录了')
            brave_time = -450
        #初始化(过关给无敌时间)
        x = 30
        y = 30
        brave = 0
        step = 0
        time = 12000
        maze = mazeData.Maze()
    if time == 0:
        box.msgbox('你已死亡\n原因:超时未通关')
        sys.exit()
        
    
    # 更新窗口
    pygame.display.flip()
    #print(x)
    #print(y)