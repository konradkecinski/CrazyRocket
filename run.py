import pygame
import sys
from rocket import Rocket
from walls import Walls


class Game(object):

    def __init__(self, lvl):
        # Config
        self.max_tps = 60.0

        # Initialization
        pygame.init()
        self.screen = pygame.display.set_mode((1280, 720))
        self.tps_clock = pygame.time.Clock()
        self.tps_delta = 0.0
        self.walls = Walls(self, lvl)
        self.player = Rocket(self)

        while True:
            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)

                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    sys.exit(0)

            # Ticking
            self.tps_delta += self.tps_clock.tick() / 1000.0
            while self.tps_delta > 1 / self.max_tps:
                self.tick()
                self.tps_delta -= 1 / self.max_tps
            # Rendering
            self.screen.fill((0, 0, 0))
            self.draw()
            pygame.display.flip()

    def tick(self):
        self.player.tick()
        self.walls.tick()

    def draw(self):
        self.player.draw()
        self.walls.draw()


if __name__ == "__main__":
    Game(2)





