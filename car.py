import pygame
import math
from utils import blit_rotate_center
import configs

class Car(object):
    
    MAX_SPEED = configs.CAR_MAX_SPEED
    ROTATION_SPEED = configs.CAR_ROTATION_SPEED
    ACCELERATION = configs.CAR_ACCELERATION
    FRICTION = configs.CAR_FRICTION
    
    def __init__(self, image, controller, track):
        self.image = image
        
        self.x = configs.START_POSITION_X
        self.y = configs.START_POSITION_Y
        self.angle = configs.START_ROTATION_ANGLE
        self.speed = 0
        
        self.track = track
        
        self.controller = controller
        
        self.engine_on = True
    
    def get_corners(self):
        half_side = self.image.get_width() / 2
        width, height = self.image.get_width(), self.image.get_height()
        center = (self.x + width/2, self.y + height/2)
        left_top = (center[0] + math.cos(math.radians(360 - (self.angle + 30))) * half_side, 
                    center[1] + math.sin(math.radians(360 - (self.angle + 30))) * half_side)
        
        right_top = (center[0] + math.cos(math.radians(360 - (self.angle + 150))) * half_side, 
                        center[1] + math.sin(math.radians(360 - (self.angle + 150))) * half_side)
        left_bottom = (center[0] + math.cos(math.radians(360 - (self.angle + 210))) * half_side, 
                        center[1] + math.sin(math.radians(360 - (self.angle + 210))) * half_side)
        right_bottom = (center[0] + math.cos(math.radians(360 - (self.angle + 330))) * half_side, 
                        center[1] + math.sin(math.radians(360 - (self.angle + 330))) * half_side)
        corners = (left_top, right_top, left_bottom, right_bottom)
        
        return corners
    
    def check_collision(self):
        corners = self.get_corners()
        
        for point in corners:
            if self.track.get_at((int(point[0]), int(point[1]))) == configs.OBSTACLE_COLOR:
                return True
        return False
    
    def move(self):
        
        # print("x",self.x, "y", self.y, "speed", self.speed, "angle", self.angle)
        
        if self.engine_on:
            self._change_xy_based_on_controller()
    
    def _change_xy_based_on_controller(self):
        # Adapted from: https://github.com/gniziemazity/Self-driving-car/blob/70b48f39000075c77bfab5cf7015774164179021/1.%20Car%20driving%20mechanics/car.js
        if self.controller['forward']:
            self.speed += self.ACCELERATION

        if self.controller['reverse']:
            self.speed-=self.ACCELERATION
        
        if self.speed > Car.MAX_SPEED:
            self.speed = Car.MAX_SPEED
        
        if self.speed < -self.MAX_SPEED/3:
            # Absolute of reverse speed cannot be
            # as much as the forward speed
            self.speed = -self.MAX_SPEED/3
        
        if self.speed > 0:
            self.speed -= self.FRICTION
            
        if self.speed < 0:
            self.speed += self.FRICTION
        
 
        if abs(self.speed)<self.FRICTION:
            self.speed=0
        
        if self.speed!=0:
            flip = 1 if self.speed>0 else -1
                
            if self.controller['left']:
                self.angle+=self.ROTATION_SPEED*flip
            
            if self.controller['right']:
                self.angle-=self.ROTATION_SPEED*flip
        
        radians = math.radians(self.angle)
        self.y -= math.cos(radians) * self.speed
        self.x -=  math.sin(radians) * self.speed
    
    def update(self, win):
        self.move()
        self.draw(win)
        
    def draw(self, win):
        blit_rotate_center(win, self.image, (self.x, self.y), self.angle)