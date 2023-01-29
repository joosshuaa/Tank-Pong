import os
from modules.collision_handler import *
from modules.event_handler import *
from modules.map_loader import *
from modules.render import *


class Combat:
    def __init__(self):
        pygame.display.set_caption(GAME_CAPTION)
        self.framerate = pygame.time.Clock()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.eventHandler = EventHandler()
        self.collision_handler = CollisionHandler()
        self.render = Render(self.screen)
        self.map_loader = MapLoader()
        self.map = []  # map rectangles
        self.relPath = os.getcwd()
        # Player instances
        bulletP1Img = pygame.image.load(self.relPath + "\\assets\\explosion1.png")
        bulletP2Img = pygame.image.load(self.relPath + "\\assets\\explosion2.png")
        self.p1 = Player(P1_POS[0], P1_POS[1], pygame.image.load(self.relPath + "\\assets\\tank1.png"), 0, bulletP1Img)
        self.p2 = Player(P2_POS[0], P2_POS[1], pygame.image.load(self.relPath + "\\assets\\tank2.png"), 180,
                         bulletP2Img)
        self.scoreP1 = Score(self.screen)
        self.scoreP2 = Score(self.screen)

    def run(self):
        pygame.init()
        # load map
        self.map = load(self.relPath + "\maps\\" + MAP)

        while True:
            # render
            self.screen.fill(MAP_BACKGROUND_COLOR)
            self.render.drawMap(self.map)
            self.render.drawPlayer(self.p1)
            self.render.drawPlayer(self.p2)
            drawScore(self.p1, self.screen, self.scoreP1, SCORE_P1_COLOR, P1_SCORE_POS[0], P1_SCORE_POS[1])
            drawScore(self.p2, self.screen, self.scoreP2, SCORE_P2_COLOR, P2_SCORE_POS[0], P2_SCORE_POS[1])
            self.p1.bullets.draw(self.screen)
            self.p2.bullets.draw(self.screen)

            # events
            event = getEvent(pygame.event.get())
            handleEvent(event, self.p1, self.p2)

            # movement
            self.p1.movement()
            self.p2.movement()
            self.p1.bullets.update()
            self.p2.bullets.update()

            # collision
            checkMapPlayerCollision(self.map, self.p1)
            checkMapPlayerCollision(self.map, self.p2)
            checkPlayerCollision(self.p1, self.p2)
            checkPlayerCollision(self.p2, self.p1)
            checkBulletMapCollision(self.p1, self.map)
            checkBulletMapCollision(self.p2, self.map)
            checkBulletPlayerCollision(self.p1, self.p2, TYPE_P2)
            checkBulletPlayerCollision(self.p2, self.p1, TYPE_P1)

            # update frame
            self.framerate.tick(FRAMERATE)
            pygame.display.flip()
