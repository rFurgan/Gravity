from enum import Enum

class COLORS(Enum):
    WHITE = (255,255,255)
    BLACK = (0,0,0)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)

class DIRECTION(Enum):
    UP="up"
    DOWN="down"
    LEFT="left"
    RIGHT="right"

G = 9.81
