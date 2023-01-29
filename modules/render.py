from modules.player import *
from modules.score import *


def drawScore(player: Player, screen, score: Score, cor, x, y):
    score.drawScore(player.score, screen, cor, x, y)


class Render:
    def __init__(self, screen) -> None:
        self.screen = screen

    def drawMap(self, map):
        for rect in map:
            pygame.draw.rect(self.screen, MAP_RECT_COLOR, rect, RECT_BORDER_SIZE)

    def drawPlayer(self, player: Player):
        self.screen.blit(player.image, player.rect)