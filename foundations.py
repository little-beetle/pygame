import pygame

pygame.init()
size = (600, 400)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Моя программа")
img = pygame.image.load("black_cat.jpg")
pygame.display.set_icon(img)

font = pygame.font.SysFont("arial", 32)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

follow = font.render("Шо ти", True, RED, GREEN)
like = font.render("Чорт", True, GREEN, BLUE)
FPS = 60
width_1, height_1 = follow.get_size()
width_2, height_2 = like.get_size()
x1, y1 = 0, 300
x2, y2 = 0, 0
direct_x1 = 1
direct_y1 = 1
direct_x2 = 1
direct_y2 = 1
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
    clock.tick(FPS)
    screen.fill(BLACK)
    screen.blit(like, (x1, y1))
    screen.blit(follow, (x2, y2))

    x1 += direct_x1
    if x1 + width_2 >= 600 or x1 < 0:
        direct_x1 =- direct_x1

    y1 += direct_y1
    if y1 + height_2 >= 400 or y1 < 0:
        direct_y1 =- direct_y1

    x2 += direct_x2
    if x2 + width_1 >= 600 or x2 < 0:
        direct_x2 =- direct_x2

    y2 += direct_y2
    if y2 + height_1 >= 400 or y2 < 0:
        direct_y2 =- direct_y2
    pygame.display.update()
