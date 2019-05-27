import pygame, sys
from levels import Levels


class Walls(object):

    def __init__(self, game, lvl):
        self.game = game
        self.levels = Levels(lvl)
        self.walls = []

    def draw(self):
        self.walls = self.levels.set_level()
        for i in self.walls:
            pygame.draw.rect(self.game.screen, (200, 50, 20), i)
            pygame.draw.rect(self.game.screen, (0, 200, 50), self.levels.stop)

    def tick(self):
        # Look for fails
        fail = False
        if 0 < self.game.player.positions[0].x > 1280:
            fail = True
        if 0 < self.game.player.positions[0].y > 720:
            fail = True
        for i in self.walls:
            if i[0] <= self.game.player.positions[0].x <= i[2]+i[0]:
                if i[1] <= self.game.player.positions[0].y <= i[3]+i[1]:
                    fail = True
            if i[0] <= self.game.player.positions[1].x <= i[2] + i[0]:
                if i[1] <= self.game.player.positions[1].y <= i[3] + i[1]:
                    fail = True
            if i[0] <= self.game.player.positions[2].x <= i[2] + i[0]:
                if i[1] <= self.game.player.positions[2].y <= i[3] + i[1]:
                    fail = True
            if fail:
                przegrales = pygame.image.load('Przegrales!.png')
                pygame.display.get_surface().blit(przegrales, (320, 200))
                pygame.display.flip()
                x = True
                while x:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            sys.exit(0)
                        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                            sys.exit(0)
                        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                            x = False
                self.game.__init__(self.levels.lvl)
        # look for wins
        i = self.levels.stop
        if i[0] <= self.game.player.positions[0].x <= i[2]+i[0]:
            if i[1] <= self.game.player.positions[0].y <= i[3]+i[1]:
                wygrales = pygame.image.load('Wygrales!.png')
                pygame.display.get_surface().blit(wygrales, (320, 200))
                pygame.display.flip()
                x = True
                while x:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            sys.exit(0)
                        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                            sys.exit(0)
                        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                            x = False
                if self.levels.lvl == 2:
                    sys.exit()
                i = self.levels.lvl + 1
                self.game.__init__(i)
