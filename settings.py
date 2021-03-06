import pygame as pg
# game options/settings
TITLE = "Midnight Adventure!"
WIDTH = 500
HEIGHT = 535
FPS = 60

# Player properties
PLAYER_ACC = 0.5
PLAYER_FRICTION = -0.09
PLAYER_GRAV = 1.0
Player_JUMP = 20

#starting platforms
PLATFORM_LIST= [(0, HEIGHT - 40, WIDTH, 40), (WIDTH /2 - 50, HEIGHT * 3 / 4, 100, 20), (125, HEIGHT - 350, 100, 20), (350, 200, 100, 20), (175, 100, 50, 20)]

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
LIGHTBLUE = (0, 155, 155)
bg = pg.image.load('Star_Night.png')
win = pg.display.set_mode((500,480))