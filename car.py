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
        self.score = 0
    
    def check_collision(self):
        width, height = self.image.get_width(), self.image.get_height()
        center = (self.x + width/2, self.y + height/2)
        
        collided = False

        if self.track.get_at((int(center[0]), int(center[1]))) == configs.OBSTACLE_COLOR:
            collided = True
            self.score -= 10
                
        self.engine_on = not collided
    
    def move(self):
        if self.engine_on:
            self._change_xy_based_on_controller()
        else:
            self.speed = 0
    
    def _change_xy_based_on_controller(self):
        # Adapted from: https://github.com/gniziemazity/Self-driving-car/blob/70b48f39000075c77bfab5cf7015774164179021/1.%20Car%20driving%20mechanics/car.js
        if self.controller['forward']:
            self.score += 5
            self.speed += self.ACCELERATION

        if self.controller['reverse']:
            self.score -= 6
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
    
    def update(self, win, **kwargs):
        self.controller.update(win, **kwargs)
        self.move()
        self.check_collision()
        self.draw(win)
        
    def draw(self, win):
        blit_rotate_center(win, self.image, (self.x, self.y), self.angle)