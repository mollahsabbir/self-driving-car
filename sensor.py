import math

import pygame

import configs
from utils import get_all_points_in_line, distance

class Sensor:
    def __init__(self, car, angle_degree):
        
        self.car = car
        
        self.angle = math.radians(angle_degree)
        # self.end_point = end_point
        self.sensor_size = configs.SENSOR_SIZE
        
        self.start_point = (0,0)
        self.end_point = (0,0)
        
        self.collision_point = (0,0)
        self.sensor_value = 0
    
    def calculate_start_point(self):
        center_x = self.car.x+self.car.image.get_width()/2
        center_y = self.car.y+self.car.image.get_height()/2
        self.start_point = (center_x, center_y)
    
    def calculate_end_point(self):
        theta = self.translate_car_angles_to_sensor_angles()
        
        x = self.start_point[0] + self.sensor_size * math.cos(theta)
        y = self.start_point[1] + self.sensor_size * math.sin(theta)
        self.end_point = (x, y)
                            
    def translate_car_angles_to_sensor_angles(self):
        return -math.radians(self.car.angle) - math.pi /2 + self.angle
    
    
    def calculate_collision_point(self):
        all_points_in_sensor = get_all_points_in_line(self.start_point, self.end_point, configs.SENSOR_SIZE)

        # Default value
        self.collision_point = self.end_point
        for point in all_points_in_sensor:   
            point_int = int(point[0]), int(point[1])  
            if self.car.track.get_at(point_int) == configs.OBSTACLE_COLOR:
                self.collision_point = (point[0], point[1])
                break
        
    def calculate_sensor_value(self):
        self.sensor_value = 1- distance(self.start_point, self.collision_point) / configs.SENSOR_SIZE
        # print(self.sensor_value)
    
    def update(self, win):
        self.calculate_start_point()
        self.calculate_end_point()
        self.calculate_collision_point()
        self.calculate_sensor_value()
        self.draw(win)
        
    def draw(self, win):
        pygame.draw.line(win, 
                        configs.SENSOR_COLOR,
                        self.start_point,
                        self.end_point)
        
        pygame.draw.line(win, 
                        configs.SENSOR_ACTIVE_COLOR,
                        self.collision_point,
                        self.end_point)
