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
follow = font.render("Шо ти",True,  RED, GREEN)
like = font.render("Чорт",True,  GREEN, BLUE)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
    screen.blit(follow, (0, 0))
    screen.blit(like, (0, 300))

    pygame.display.update()