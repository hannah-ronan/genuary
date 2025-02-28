import pygame
import math
import cv2
import numpy as np
import time

class Object:
    def __init__(self, _points, _edges):
        self.points = _points
        self.edges = _edges
        self.origin = np.average(np.array(_points), axis = 0)

    def rotate_z(self, angle):
        for i in range (len(self.points)):
            point = self.points[i]
            point = (point[0]-self.origin[0], point[1]-self.origin[1], point[2])
            self.points[i] = ((point[0]*math.cos(angle)) - (point[1]*math.sin(angle)) + self.origin[0], (point[1]*math.cos(angle)) + (point[0]*math.sin(angle)) + self.origin[1], point[2])
            
    def draw(self, color):
        projected_points = project_points(self.points)
        for edge in self.edges:
            pygame.draw.line(screen, color, projected_points[edge[0]], projected_points[edge[1]])
        pygame.display.flip()

def project_points(points):
    # Define the camera matrix 
    focal_length = 300
    camera_matrix = np.array([[focal_length, 0, img_size[0]//2], 
                            [0, focal_length, img_size[1]//2], 
                            [0, 0, 1]], np.float32) 
    
    
    # Define the distortion coefficients 
    dist_coeffs = np.zeros((5, 1), np.float32) 
    
    # Define the 3D point in the world coordinate system 
    points_3d = np.array([points], np.float32)
    
    # Define the rotation and translation vectors 
    rvec = np.array([1,0,0], np.float32)
    tvec = np.array([-75,30,0], np.float32)
    
    # Map the 3D point to 2D point 
    points_2d, _ = cv2.projectPoints(points_3d, 
                                    rvec, tvec, 
                                    camera_matrix, 
                                    dist_coeffs) 
    return [(int(point[0][0]), int(point[0][1]))for point in points_2d]

img_size = (500,500)
screen = pygame.display.set_mode((img_size[0], img_size[1]))
rads_p_sec = 1
cube_scale = 100

cube_points = [(1,1,1),(1,0.5,1),(0.5,0.5,1),(0.5,1,1),(1,1,0.5),(1,0.5,0.5),(0.5,0.5,0.5),(0.5,1,0.5)]
cube_points = [(point[0]*cube_scale, point[1]* cube_scale, point[2] * cube_scale) for point in cube_points]
cube_edges = [(0,1),(1,2),(2,3),(3,0),(4,5),(5,6),(6,7),(7,4),(0,4),(1,5),(2,6),(3,7)]
cube = Object(cube_points, cube_edges)

last_loop_time = time.time()
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    screen.fill((0,0,0))
    timediff = time.time() - last_loop_time
    last_loop_time = time.time()
    cube.rotate_z(rads_p_sec * timediff)
    cube.draw((255,0,0))

pygame.image.save(screen,"3d_output.png")
pygame.quit()