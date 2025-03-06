#created for https://genuary.art/ prompt #6: Make a landscape using only primitive shapes.
import pygame
from PIL import Image, ImageColor

pygame.init()
img_size = (500,500)
wallpaper_dim = (2532, 2532)
screen = pygame.display.set_mode(img_size)
new_pixel_size = 5
spacing = 1.2
pallete_f_name = "comfy52.hex" #https://lospec.com/palette-list/comfy52
input_f_name = "6_input(3).png"
pallete = []


with open(pallete_f_name, "r") as file:
    for line in file:
        pallete.append(ImageColor.getcolor(f"#{line[:6]}","RGB"))

def color_distance(a,b):
    return abs(a[0]-b[0])+abs(a[1]-b[1])+abs(a[2]-b[2]) 

def color_shape(color):
    r = color[0]
    g = color[1]
    b = color[2]
    return "circle" if b > r and b > g else "triangle" if g > r and g > b else "square"

input = Image.open(input_f_name)
for i,p in enumerate(input.getdata()):
    x = i % img_size[0]
    y = (i - x)//img_size[1]

    if x % (new_pixel_size*spacing) == 0 and y % (new_pixel_size*spacing) == 0:
        closest_color = pallete[0]
        smallest_distance = color_distance(p,closest_color)
        for color in pallete:
            curr_distance = color_distance(p, color)
            if curr_distance < smallest_distance:
                closest_color = color
                smallest_distance = curr_distance
        shape = color_shape(closest_color)
        match shape:
            case "circle":
                pygame.draw.circle(screen, closest_color, (x,y), new_pixel_size//2)
            case "square":
                pygame.draw.rect(screen, closest_color, pygame.Rect(x-new_pixel_size//2, y-new_pixel_size//2, new_pixel_size,new_pixel_size), new_pixel_size)
            case "triangle":
                pygame.draw.polygon(screen, closest_color, [(x, y - new_pixel_size//2), (x + new_pixel_size//2,y + new_pixel_size//2),(x - new_pixel_size//2,y + new_pixel_size//2)])
            case _:
                pass

pygame.image.save(screen, "6_output.png")
pygame.quit()