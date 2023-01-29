import pygame
from config.settings import *


def loadMapCoordinates(path):
    coordinates = []
    with open(path) as file:
        for indexY, line in enumerate(file):
            for indexX, columnar in enumerate(line):
                if columnar == MAP_CHAR:
                    coordinates.append((indexX+1, indexY+1))
    return coordinates


def generateMapRects(coords):
    rects = []
    for coord in coords:
        rects.append(
            pygame.Rect(coord[0]*MULTI_FACTOR,
                        coord[1]*MULTI_FACTOR+OFFSET_Y,
                        MAP_RECT_X*MULTI_FACTOR,
                        MAP_RECT_Y*MULTI_FACTOR))
    return rects


def load(path):
    coord = loadMapCoordinates(path)
    mapRects = generateMapRects(coord)
    return mapRects


class MapLoader:
    def __init__(self) -> None:
        pass

