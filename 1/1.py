#created for https://genuary.art/ prompt #1: Vertical or horizontal lines only.

import pygame
from PIL import Image
import random

input_file = "1_input(2).png"
block_size = int(10)
img_size = 500
block_count = img_size//block_size
colors = {"R":(255,0,0),
          "G":(0,255,0),
          "B":(0,0,255)}
color_order = ["R","B","G"]

pygame.init()
screen = pygame.display.set_mode((img_size, img_size))
screen.fill((255, 255, 255))

def map_value(val,src,dst):
    return ((val - src[0]) / (src[1]-src[0])) * (dst[1]-dst[0]) + dst[0]

def draw_block(x,y,line_weight, line_spacing, color):
    dir = "v" if random.randint(0,1) == 0 else "h"
    if dir == "v":
        lc = block_size // (line_weight + line_spacing)
        for i in range(lc):
            sp = x + (i*line_weight) + (i*line_spacing)
            pygame.draw.line(screen, color, (sp,y),(sp,y+block_size), line_weight)
    else:
        lc = block_size // (line_weight + line_spacing)
        for i in range(lc):
            sp = y + (i*line_weight) + (i*line_spacing)
            pygame.draw.line(screen, color, (x,sp),(x+block_size,sp), line_weight)


img = Image.open(input_file)
img = img.resize((block_count, block_count))
screen.fill(img.resize((1,1)).getdata()[0])
img = img.convert("RGB")

for ch in color_order:
    band = img.getchannel(ch)
    color = colors[ch]
    pixels = band.getdata()
    for y in range(block_count):
        for x in range(block_count):
            idx = x + (y * block_count)
            p = pixels[idx]
            lw = int(map_value(p, (0,255), (0, block_size//2)))
            ls = int(map_value(lw, (0, block_size//2), (block_size//2,1)))
            if lw > 0:
                draw_block(x * block_size,y * block_size, lw,ls, color)

pygame.image.save(screen, "1_output.png")
pygame.quit()

