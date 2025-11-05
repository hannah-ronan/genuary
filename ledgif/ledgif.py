import pygame
from PIL import Image
import math
import glob

def gradient_circle(start_color, goal_color, radius, loc):
    offset = 0
    mid_color = start_color[:]
    for y in range(loc[1]-radius, loc[1]+radius,1):
        for x in range(loc[0]-radius, loc[0]+radius,2):
            distance = math.sqrt(pow(x - loc[0],2) + pow(y - loc[1],2))
            if distance <= radius:
                mid_color = [map_value(distance, (0,radius), (start_color[i], goal_color[i])) for i in range(3)]
                pygame.draw.line(screen,mid_color,(x + offset,y),(x + offset,y))
        offset = 1 if offset == 0 else 0

def map_value(val,src,dst):
    return ((val - src[0]) / (src[1]-src[0])) * (dst[1]-dst[0]) + dst[0]

def scale_color(start_color):
    scaled_color =  [x * centre_brightness_scale for x in list(start_color)]
    for i, channel in enumerate(scaled_color):
        if channel>255:
            scaled_color[i] = 255
    return tuple(scaled_color)

input_file = "input.gif"
final_res = (30,30)
loops = 30
scale = 20
centre_brightness_scale = 5

img = Image.open(input_file)
frames = []

print("initiating pygame...")
pygame.init()
screen = pygame.display.set_mode((final_res[0]*scale, final_res[1]*scale))
screen.fill((50, 50, 50))
print("pygame initiated...")

print("getting frames...")
try:
    while True:
        frame = img.resize((final_res[0], final_res[1]))
        frames.append(frame)
        img.seek(img.tell() + 1) 

except EOFError:
    pass

def generate_frames():
    print("displaying frames...")
    for i,frame in enumerate(frames[1:]):
        print(f"displaying frame {i}...")
        pixels = frame.getdata()
        for y in range(final_res[1]):
            for x in range(final_res[0]):
                idx = x + (y * final_res[0])
                p = pixels[idx]
                radius = scale//2
                loc = ((x*scale)+(radius), (y*scale)+(radius))
                #pygame.draw.circle(screen, p, loc, radius)
                gradient_circle(scale_color(p), p, radius, loc)
        pygame.image.save(screen, f"frames/output_{i}.png")

def save_frames():
    print("saving frames...")
    frames = [Image.open(image) for image in glob.glob(f"frames/*.png")]
    frame_one = frames[0]
    frame_one.save("output.gif", format="GIF", append_images=frames, save_all=True, duration=100, loop=0)
    
generate_frames()
save_frames()