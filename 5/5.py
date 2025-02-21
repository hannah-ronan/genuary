#created for https://genuary.art/ prompt #5: Isometric Art (No vanishing points).
from collections import namedtuple
import pygame
import math
import random

Point = namedtuple("Point",["x","y"])
Cube = namedtuple("Cube",["l","w","h"])
colors = [(192, 192, 192), (117, 117, 117), (168, 169, 173), (130,130,130)]

img_size = (500,500)
scalef = 0.7
pygame.init()
screen = pygame.display.set_mode((img_size[0], img_size[1]))
screen.fill((20,20,20))

def rotate_point(origin, point, angle):
    translated_point = Point(x = point.x - origin.x, y = point.y - origin.y)
    rotated_point =  Point(x = (translated_point.x * math.cos(angle)) - (translated_point.y * math.sin(angle)), y = (translated_point.y * math.cos(angle)) + (translated_point.x * math.sin(angle)))
    return Point(x = rotated_point.x + origin.x, y = rotated_point.y + origin.y)

def draw_building(loc, size, color):
    corners = [loc, Point(x = loc.x + size.l, y = loc.y),Point(x = loc.x + size.l, y = loc.y + size.w),Point(x = loc.x, y = loc.y + size.w)]
    for i in range(1,4):
        corners[i] = rotate_point(loc, corners[i], -math.pi/4)
        corners[i] = Point(x = corners[i].x, y = ((corners[i].y - loc.y) * scalef) + loc.y)
    
    roof_points = [(p.x, p.y - size.h) for p in corners]
    front_points = [corners[3], corners[0], (corners[0].x, corners[0].y-size.h),(corners[3].x, corners[3].y-size.h)]
    side_points = [corners[2], corners[3], (corners[3].x, corners[3].y-size.h), (corners[2].x, corners[2].y-size.h)]

    pygame.draw.polygon(screen, (color[0]*0.8, color[1]*0.8, color[2]*0.8), side_points)
    pygame.draw.polygon(screen, color, front_points)
    pygame.draw.polygon(screen, color, roof_points)

done = False
current_y = 0
while not done:
    size = Cube(l = random.randint(40,100), w = random.randint(40,100), h = random.randint(60,200))
    color = colors[random.randint(0,len(colors)-1)]
    draw_building(Point(x = random.randint(5, img_size[0]-5-size.l), y = current_y), size, color)
    current_y += 15
    if current_y > img_size[1] - 5:
        done = True

pygame.image.save(screen, "5_output.png")
