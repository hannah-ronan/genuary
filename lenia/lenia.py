import pygame
from PIL import Image
import math
import time

def map_value(val,src,dst):
    return ((val - src[0]) / (src[1]-src[0])) * (dst[1]-dst[0]) + dst[0]

def clamp(value, min_val, max_val):
    if value < min_val:
        return min_val
    elif value > max_val:
        return max_val
    else:
        return value

class Kernel:

    def __init__(self, mask_img, initial_config_img):
        print("initiating kernel...")
        self.kernel_max = 0
        self.mask = self.process_image(mask_img, True)
        self.initial_config = self.process_image(initial_config_img, False)

    def process_image(self, img, is_mask):
        width, height = img.size
        grid = [[0 for i in range(width)] for j in range(height)]
        pixels = img.getdata()
        for y in range(height):
            for x in range(width):
                idx = x + (y*width)
                p = pixels[idx][0] 
                p = map_value(p, (0,255), (0,1))
                if is_mask:
                    self.kernel_max+= p
                grid[y][x] = p
        return grid
    

class Channel:
    def __init__(self, kernel, growth_center, growth_range, delta_t, screen):
        print("initiating channel...")
        self.kernel = kernel
        self.growth_center = growth_center
        self.growth_range = growth_range
        self.delta_t = delta_t
        self.screen = screen
        self.width, self.height = screen.get_size()
        self.cells = [[Cell((i,j), 0) for i in range(self.width)] for j in range(self.height)]
        self.init_cells(kernel)

    def init_cells(self, kernel):
        print("initiating cells...")
        mask_midpoint = (math.ceil(len(kernel.mask[0])/2), math.ceil(len(kernel.mask)/2))
        for y in range(len(self.cells)):
            for x in range(len(self.cells[0])):
                self.cells[y][x].value = kernel.initial_config[y][x]
                for y_offset, m_y in enumerate(kernel.mask):
                    for x_offset, m_x in enumerate(m_y):
                        if m_x > 0:
                            try:
                                neighbour_x = x - mask_midpoint[0] + x_offset
                                neighbour_y = y - mask_midpoint[1] + y_offset
                                if neighbour_y >= 0 and neighbour_x >= 0 and not(neighbour_x == x and neighbour_y == y): #don't check any negative indices, or the current cell
                                    before = y_offset < mask_midpoint[1] or (x_offset < mask_midpoint[0] and y_offset < mask_midpoint[1])
                                    relative_cell = self.cells[neighbour_y][neighbour_x]
                                    new_neighbour = Neighbour(relative_cell, m_x, before)
                                    self.cells[y][x].neighbours.append(new_neighbour)
                            except:
                                pass

    def growth_func(self, cell):
        cell_neighbour_sum = cell.sum_neighbours()
        normalized_sum = cell_neighbour_sum/self.kernel.kernal_max
        if abs(normalized_sum - self.growth_center) < self.growth_range:
            x = (normalized_sum - self.growth_center) / self.growth_range
            f = math.exp(-1 / (1 - x**2)) / math.exp(-1)
            return f - 0.5
        else:
            return -0.5

        
    def step(self):
        print("running step...")
        self.screen.fill((0,0,0))
        for row in self.cells:
            for cell in row:
                cell.prev_value = cell.value
                growth = self.growth_func(cell)
                growth = growth * self.delta_t
                cell.value = clamp(cell.value + growth, 0, 1)
                color = map_value(cell.value, (0,1), (0,255))
                pygame.draw.line(self.screen, (color,color,color), cell.location, cell.location)
        pygame.display.flip()


class Neighbour:
    def __init__(self, cell, weight, before):
        self.weight = weight
        self.cell = cell
        self.before = before

class Cell:
    def __init__(self, location, value):
        self.location = location
        self.value = value
        self.neighbours = []
        self.prev_value = 0

    def sum_neighbours(self):
        neighbour_sum = 0
        for neighbour in self.neighbours:
            if neighbour.before:
                neighbour_sum += neighbour.cell.prev_value * neighbour.weight
            else:
                neighbour_sum += neighbour.cell.value * neighbour.weight
        return neighbour_sum

file_path = "C:/Users/hanna/OneDrive/Documents/Programming_Projects/genuary/lenia/"
steps = 100

mask_img = Image.open(f"{file_path}masks/radial_gradient.png")
initial_config_img = Image.open(f"{file_path}initial_configs/medium.png")
new_kernel = Kernel(mask_img, initial_config_img)
print(f"kernel max: {new_kernel.kernel_max}")

pygame.init()
screen = pygame.display.set_mode(initial_config_img.size)
screen.fill((0, 0, 0))


new_game = Channel(new_kernel, 0.5, 0.4, 0.1, screen)

for i in range(steps):
    new_game.step()
    time.sleep(0.05)

pygame.image.save(screen,f"{file_path}lenia_output.png")

pygame.quit()
