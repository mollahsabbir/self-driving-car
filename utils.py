import pygame
import numpy as np

def blit_rotate_center(win, image, top_left, angle):
    # Source: https://stackoverflow.com/a/54714144
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(
        center=image.get_rect(topleft=top_left).center)
    win.blit(rotated_image, new_rect.topleft)
    
def get_all_points_in_line(start_point, end_point, divisions):
    xs = np.linspace(start_point[0], end_point[0], divisions+1)
    ys = np.linspace(start_point[1], end_point[1], divisions+1)
    
    return list(zip(xs,ys))

def distance(point1, point2):
    point1, point2 = np.array(point1), np.array(point2)
    return np.linalg.norm(point1 - point2)