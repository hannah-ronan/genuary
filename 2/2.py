#created for https://genuary.art/ prompt #2: Layers upon layers upon layers.

from perlin_noise import PerlinNoise
from PIL import Image
import matplotlib.pyplot as plt


img_size = 500
input_file = "2_input.png"

steps = [0,59,119,185,255]


def map_value(val,src,dst):
    return ((val - src[0]) / (src[1]-src[0])) * (dst[1]-dst[0]) + dst[0]

def create_mask(lower_bound, upper_bound):
    mask = Image.new("L", (img_size,img_size))
    for y in range(img_size):
        for x in range(img_size):
            noise_v = noise_values[x + (y * img_size)]
            if lower_bound <= noise_v <= upper_bound:
                mask.putpixel((x,y), int(map_value(noise_v, (lower_bound,upper_bound), (0,255))))
    return mask.convert("1")

def remove_channels(image,channels):
    new_img = Image.new("RGBA", (img_size,img_size))
    new_data = []
    for p in image.getdata():
        new_p = list(p)
        for c in channels:
            new_p[c] = 0
        new_data.append(tuple(new_p))
    new_img.putdata(new_data)
    return new_img

noise = PerlinNoise(octaves=3)
noise_values = [map_value(noise([i/img_size, j/img_size]), (-0.5,0.5), (0,255)) for j in range(img_size) for i in range(img_size)]

masks = []

for i in range(4):
    masks.append(create_mask(steps[i], steps[i+1]))

img = Image.open(input_file)
img = img.convert("RGBA")

l1 = img.copy()
l2 = img.resize((img_size//8, img_size//8)).resize((img_size,img_size),0)
l3 = img.resize((img_size//16, img_size//16)).resize((img_size,img_size),0)
l4 = img.resize((img_size//32, img_size//32)).resize((img_size,img_size),0)

img.paste(l4, (0,0), masks[3])
img.paste(l3, (0,0), masks[2])
img.paste(l2, (0,0), masks[1])
img.paste(l1, (0,0), masks[0])
 
img.save("2_output.png")