import pygame
from pygame.math import Vector2


class Rocket(object):

    def __init__(self, game):
        self.game = game
        self.speed = 1.3
        self.gravity = 0.5
        self.pos = Vector2(game.walls.levels.start[0], game.walls.levels.start[1])
        self.vel = Vector2(0, 0)
        self.acc = Vector2(0, 0)
        self.positions = None

    def add_force(self, force):
            self.acc += force

    def tick(self):
        # Physic
        self.vel *= 0.8
        self.vel -= Vector2(0, -self.gravity)
        self.vel += self.acc
        self.pos.x += self.vel.x
        self.pos.y += self.vel.y
        self.acc *= 0
        # Checking inputs
        keys = pygame.key.get_pressed()
        x = 1
        if keys[pygame.K_SPACE]:
            x = 5
        if keys[pygame.K_d]:
            self.add_force(Vector2(self.speed*x, 0))
        if keys[pygame.K_a]:
            self.add_force(Vector2(-self.speed*x, 0))
        if keys[pygame.K_w]:
            self.add_force(Vector2(0, -self.speed*x))
        if keys[pygame.K_s]:
            self.add_force(Vector2(0, self.speed*x))
    def draw(self):
        # Base triangle and fire
        points = [Vector2(0, -30), Vector2(15, 15), Vector2(-15, 15)]
        fire_1 = [Vector2(15, 30), Vector2(12, 15)]
        fire_2 = [Vector2(12, 30), Vector2(9, 15)]
        fire_3 = [Vector2(9, 30), Vector2(6, 15)]
        fire_4 = [Vector2(5, 30), Vector2(3, 15)]
        fire_5 = [Vector2(0, 30), Vector2(0, 15)]
        fire_6 = [Vector2(-5, 30), Vector2(-3, 15)]
        fire_7 = [Vector2(-8, 30), Vector2(-5, 15)]
        fire_8 = [Vector2(-11, 30), Vector2(-8, 15)]
        fire_9 = [Vector2(-14, 30), Vector2(-11, 15)]
        # Rotate points
        angle = self.vel.angle_to(Vector2(0, 1))
        points = [p.rotate(angle) for p in points]
        fire_1 = [p.rotate(angle) for p in fire_1]
        fire_2 = [p.rotate(angle) for p in fire_2]
        fire_3 = [p.rotate(angle) for p in fire_3]
        fire_4 = [p.rotate(angle) for p in fire_4]
        fire_5 = [p.rotate(angle) for p in fire_5]
        fire_6 = [p.rotate(angle) for p in fire_6]
        fire_7 = [p.rotate(angle) for p in fire_7]
        fire_8 = [p.rotate(angle) for p in fire_8]
        fire_9 = [p.rotate(angle) for p in fire_9]
        # Fix y axis
        points = [Vector2(p.x, p.y*-1) for p in points]
        fire_1 = [Vector2(p.x, p.y * -1) for p in fire_1]
        fire_2 = [Vector2(p.x, p.y * -1) for p in fire_2]
        fire_3 = [Vector2(p.x, p.y * -1) for p in fire_3]
        fire_4 = [Vector2(p.x, p.y * -1) for p in fire_4]
        fire_5 = [Vector2(p.x, p.y * -1) for p in fire_5]
        fire_6 = [Vector2(p.x, p.y * -1) for p in fire_6]
        fire_7 = [Vector2(p.x, p.y * -1) for p in fire_7]
        fire_8 = [Vector2(p.x, p.y * -1) for p in fire_8]
        fire_9 = [Vector2(p.x, p.y * -1) for p in fire_9]
        # Add current position
        points = [self.pos+p for p in points]
        fire_1 = [self.pos + p for p in fire_1]
        fire_2 = [self.pos + p for p in fire_2]
        fire_3 = [self.pos + p for p in fire_3]
        fire_4 = [self.pos + p for p in fire_4]
        fire_5 = [self.pos + p for p in fire_5]
        fire_6 = [self.pos + p for p in fire_6]
        fire_7 = [self.pos + p for p in fire_7]
        fire_8 = [self.pos + p for p in fire_8]
        fire_9 = [self.pos + p for p in fire_9]
        # Draw triangle
        pygame.draw.polygon(self.game.screen, (0, 100, 255), points)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d] or keys[pygame.K_a] or keys[pygame.K_w] or keys[pygame.K_s]:
            pygame.draw.line(self.game.screen, (200, 0, 100), fire_1[0], fire_1[1])
            pygame.draw.line(self.game.screen, (200, 0, 100), fire_2[0], fire_2[1])
            pygame.draw.line(self.game.screen, (200, 0, 100), fire_3[0], fire_3[1])
            pygame.draw.line(self.game.screen, (200, 0, 100), fire_4[0], fire_4[1])
            pygame.draw.line(self.game.screen, (200, 0, 100), fire_5[0], fire_5[1])
            pygame.draw.line(self.game.screen, (200, 0, 100), fire_6[0], fire_6[1])
            pygame.draw.line(self.game.screen, (200, 0, 100), fire_7[0], fire_7[1])
            pygame.draw.line(self.game.screen, (200, 0, 100), fire_8[0], fire_8[1])
            pygame.draw.line(self.game.screen, (200, 0, 100), fire_9[0], fire_9[1])
        self.positions = points
