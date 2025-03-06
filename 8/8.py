#created for https://genuary.art/ prompt #8: Draw one million of something.
import pygame
from random import randint

img_size = (500,500)
pygame.init()
screen = pygame.display.set_mode(img_size)

for i in range(1000000):
    pygame.draw.line(screen, (randint(0,255),255,255), (randint(0,img_size[0]), randint(0,img_size[1])),  (randint(0,img_size[0]), randint(0,img_size[1])), 1)
    pygame.draw.circle(screen, (255,0,randint(0,255)), (randint(0,img_size[0]), randint(0,img_size[1])), randint(5,50), 1)

pygame.image.save(screen, "8_output.png")