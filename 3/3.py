import pygame
import math
import random
from PIL import Image

pygame.init()
img_size = (500,500)
wallpaper_dim = (500, 500)
screen = pygame.display.set_mode((img_size[0], img_size[1]))
cmyk = [[0,255,255],[255,0,255],[255,255,0]]

def map_value(val,src,dst):
    return ((val - src[0]) / (src[1]-src[0])) * (dst[1]-dst[0]) + dst[0]

def gradient_circle(start_color, goal_color, radius, loc):
    offset = 0
    mid_color = start_color[:]
    for y in range(loc[1]-radius, loc[1]+radius,2):
        for x in range(loc[0]-radius, loc[0]+radius,2):
            distance = math.sqrt(pow(x - loc[0],2) + pow(y - loc[1],2))
            if distance <= radius:
                mid_color = [map_value(distance, (0,radius), (start_color[i], goal_color[i])) for i in range(3)]
                pygame.draw.line(screen,mid_color,(x + offset,y),(x + offset,y))
        offset = 1 if offset == 0 else 0

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                screen.fill((255,255,255))
                pygame.display.flip()
                for i in range(20):
                    gradient_circle(cmyk[random.randint(0,2)],cmyk[random.randint(0,2)], random.randint(50,250), (random.randint(0,img_size[0]),random.randint(0,img_size[1])))
                pygame.display.flip()
            elif event.key == pygame.K_s:
                pygame.image.save(screen, "3_output.png")
                pygame.quit()
                output = Image.open("3_output.png").resize(wallpaper_dim, 0).save("3_output.png")
                run = False