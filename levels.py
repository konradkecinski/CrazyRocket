

class Levels(object):

    def __init__(self, lvl):
        if lvl == 0:
            self.start = (40, 40)
        if lvl == 1:
            self.start = (900, 360)
        if lvl == 2:
            self.start = (50, 50)
        self.stop = (0, 0, 0, 0)
        self.lvl = lvl

    def set_level(self):
        if self.lvl == 0:
            self.stop = (1090, 10, 180, 30)
            walls = []
            walls.append((0, 0, 10, 720))
            walls.append((1270, 0, 10, 720))
            walls.append((0, 0, 1280, 10))
            walls.append((0, 710, 1280, 10))
            walls.append((190, 10, 180, 600))
            walls.append((550, 130, 180, 600))
            walls.append((910, 10, 180, 600))
            return walls
        if self.lvl == 1:
            self.stop = (1080, 530, 80, 30)
            walls = []
            walls.append((0, 0, 10, 720))
            walls.append((1270, 0, 10, 720))
            walls.append((0, 0, 1280, 10))
            walls.append((0, 710, 1280, 10))
            walls.append((90, 560, 1100, 30))
            walls.append((1160, 320, 30, 250))
            walls.append((1050, 0, 30, 580))
            walls.append((500, 100, 200, 480))
            walls.append((0, 0, 200, 400))
            return walls
        if self.lvl == 2:
            self.stop = (1000, 290, 40, 180)
            walls = []
            walls.append((0, 0, 10, 720))
            walls.append((1270, 0, 10, 720))
            walls.append((0, 0, 1280, 10))
            walls.append((0, 710, 1280, 10))
            walls.append((90, 0, 40, 630))
            walls.append((130, 590, 1060, 40))
            walls.append((1150, 130, 40, 500))
            walls.append((210, 130, 40, 380))
            walls.append((210, 130, 980, 40))
            walls.append((210, 470, 860, 40))
            walls.append((1040, 250, 40, 260))
            walls.append((330, 250, 720, 40))
            walls.append((330, 290, 40, 100))
            walls.append((450, 370, 40, 100))
            walls.append((570, 290, 40, 100))
            walls.append((690, 370, 40, 100))
            return walls
