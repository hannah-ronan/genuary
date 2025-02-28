#this doesnt have to do with genuary, just something I saw that I wanted to recreate: https://github.com/chilledwilba/Lissajous-Curve/blob/master/Pics/Normal.gif
import time
import math
import pygame

x_rads_p_sec = 10
y_rads_p_sec = 14
trail_length = 2000

x_loc = (400,250)
y_loc = (400,250)
origin = (250, 250)

def rot_point(point, angle):
    point = (point[0] - origin[0], point[1] - origin[1])
    point = ((point[0]*math.cos(angle)) - (point[1]*math.sin(angle)), (point[1]*math.cos(angle)) + (point[0]*math.sin(angle)))
    return (point[0] + origin[0], point[1] + origin[1])

img_size = (500,500)
screen = pygame.display.set_mode((img_size[0], img_size[1]))

last_loop_time = time.time()
trail = [(x_loc[0], y_loc[1])]

run = True
while run:
    screen.fill((0,0,0))
    timediff = time.time() - last_loop_time
    last_loop_time = time.time()
    x_loc = rot_point(x_loc, x_rads_p_sec * timediff)
    y_loc = rot_point(y_loc, y_rads_p_sec * timediff)

    if len(trail) == trail_length:
        trail.pop()
    trail.insert(0, (x_loc[0], y_loc[1]))
    for i in range(1, len(trail)):
        pygame.draw.line(screen, (255,0,0), (trail[i-1]), trail[i])    
    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.image.save(screen,"tangent_output.png")
pygame.quit()