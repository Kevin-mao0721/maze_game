import pygame
import random
import os

# 加载宝物图片
path = os.path.dirname(os.path.realpath(__file__))
imgPath = path + '/images/'
treasure = []
for i in range(1, 8):
    treasure.append(pygame.image.load(imgPath + str(i) + '.png'))


# 迷宫（使用prim方法，节点列表存储路）
class Maze:
    # 初始化迷宫
    # width：迷宫中横向路的数量
    # height：迷宫中纵向路的数量
    def __init__(self):
        # 路的大小
        self.size = [20, 11]   #原来   self.size = [12, 12]
        # 整个迷宫的大小为：（2 * width + 1, 2 * height + 1），迷宫包括路和墙
        # 使用二维数组表示迷宫，0表示墙， 1表示路
        # 首先全部定义为墙
        self.map = [[0 for w in range(2 * self.size[0] + 1)] for h in range(2 * self.size[1] + 1)]
        # 随机选取一个原本是路的墙作为起始开拓点
        startX = random.choice(range(self.size[0]))
        startY = random.choice(range(self.size[1]))
        # 将这个开拓点打通
        self.map[2 * startY + 1][2 * startX + 1] = 1
        # 将选取的开拓点加入节点列表
        self.roadList = [[startX, startY]]
        # 开拓迷宫
        self.setMap()
        # 设置迷宫单元
        self.unit = [30, 30]
        # 设置迷宫终点
        self.end = [(2 * self.size[0] + 1 - 1) * self.unit[0], (2 * self.size[1] + 1 - 1 - 1) * self.unit[1]]
        # 宝物图片
        self.treasure = treasure[random.randint(0, 6)]


    # 开拓迷宫
    def setMap(self):
        # 当节点列表不为空时
        while self.roadList:
            # 随机选取一个节点（路）
            road = random.choice(self.roadList)
            # 判断这个路的上下左右是否有未访问（值为0）的路
            directionList = self.getRoundRoad(road)
            if directionList:
                # 随机选取一个方向的路打通，并将选取的路加入节点列表
                self.getThrough(road, directionList)
            else:
                # 上下左右的路都访问过了，则将该路移出节点列表
                # 当节点列表为空时，也就每个路都访问过一遍了
                self.roadList.remove(road)

    # 判断路的上下左右是否有未被访问过的路
    def getRoundRoad(self, road):
        x, y = road
        directionList = []
        if x > 0:
            if self.map[2 * y + 1][2 * (x - 1) + 1] == 0:
                directionList.append('left')
        if x < self.size[0] - 1:
            if self.map[2 * y + 1][2 * (x + 1) + 1] == 0:
                directionList.append('right')
        if y > 0:
            if self.map[2 * (y - 1) + 1][2 * x + 1] == 0:
                directionList.append('up')
        if y < self.size[1] - 1:
            if self.map[2 * (y + 1) + 1][2 * x + 1] == 0:
                directionList.append('down')

        return directionList

    # 打通两条路之间的墙，并将新打通的路加入节点列表
    def getThrough(self, road, directionList):
        x, y = road
        direction = random.choice(directionList)
        if direction == 'up':
            self.map[2 * (y - 1) + 1][2 * x + 1] = 1
            self.map[2 * y][2 * x + 1] = 1
            self.roadList.append([x, y - 1])
        elif direction == 'down':
            self.map[2 * (y + 1) + 1][2 * x + 1] = 1
            self.map[2 * (y + 1)][2 * x + 1] = 1
            self.roadList.append([x, y + 1])
        elif direction == 'left':
            self.map[2 * y + 1][2 * (x - 1) + 1] = 1
            self.map[2 * y + 1][2 * x] = 1
            self.roadList.append([x - 1, y])
        elif direction == 'right':
            self.map[2 * y + 1][2 * (x + 1) + 1] = 1
            self.map[2 * y + 1][2 * (x + 1)] = 1
            self.roadList.append([x + 1, y])

    # 格式化输出
    def printMap(self):
        string = ''
        for y in self.map:
            for x in y:
                string = string + str(x) + ' '
            string += '\n'

        print(string)

    # 绘制迷宫
    def draw(self, screen):
        # 绘制迷宫的地图
        for row in range(len(self.map)):
            for col in range(len(self.map[row])):
                if self.map[row][col] == 1:
                    pygame.draw.rect(screen, [255, 255, 255], [col * self.unit[0], row * self.unit[1], self.unit[0], self.unit[1]])

        # 绘制终点标识（宝物）
        screen.blit(self.treasure, self.end)

        # # 绘制终点标识（小旗）
        # pygame.draw.rect(screen, [255, 255, 255], [self.end[0], self.end[1], self.unit[0], self.unit[1]])
        #
        # pygame.draw.line(screen,
        #                  [0, 255, 0],
        #                  [self.end[0] + int(self.unit[0] / 4), self.end[1] + int(self.unit[1] / 5)],
        #                  [self.end[0] + int(self.unit[0] / 4), self.end[1] + int(self.unit[1] * 4 / 5)])
        # pygame.draw.rect(screen,
        #                  [0, 255, 0],
        #                  [self.end[0] + int(self.unit[0] / 4), self.end[1] + int(self.unit[1] / 5), int(self.unit[0] / 2), int(self.unit[1] / 3)])

if __name__ == '__main__':
    maze = Maze()
    maze.printMap()
