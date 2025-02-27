#this doesnt have to do with genuary, just something I saw that I wanted to recreate: https://github.com/chilledwilba/Lissajous-Curve/blob/master/Pics/Normal.gif
import time
import math
import pygame

x_degrees_p_sec = 5
y_degrees_p_sec = 7

x_loc = (250,0)
y_loc = (250,0)
origin = (250, 250)
loops = 5000

def rot_point(point, angle):
    point = (point[0] - origin[0], point[1] - origin[1])
    return ((point[0]*math.cos(angle)) - (point[1]*math.sin(angle)) + origin[0], (point[1]*math.cos(angle)) + (point[0]*math.sin(angle)) + origin[1])

img_size = (500,500)
screen = pygame.display.set_mode((img_size[0], img_size[1]))

last_loop_time = time.time()
for i in range(loops):
    timediff = time.time() - last_loop_time
    pygame.draw.line(screen, (255,0,0), (x_loc[0], y_loc[1]),(x_loc[0],y_loc[1]))
    x_loc = rot_point(x_loc, x_degrees_p_sec * timediff)
    y_loc = rot_point(y_loc, y_degrees_p_sec * timediff)
    pygame.display.flip()

pygame.image.save(screen,"tangent_output.png")
pygame.quit()