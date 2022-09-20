import pygame
import sys
import time
import math
import configs

from car import Car
from controllers import KeyboardController
from eventhandler import EventHandler, GameExitEventListener

if __name__ == "__main__":
    
    track = pygame.image.load(configs.TRACK_IMAGE)
    car_image = pygame.image.load(configs.CAR_IMAGE)
    
    kb_controller = KeyboardController()
    car = Car(car_image, kb_controller)
    
    
    win_width, win_height = track.get_width(), track.get_height()
    win = pygame.display.set_mode((win_width, win_height))
    pygame.display.set_caption("Self Driving Car")
    
    event_listeners = [GameExitEventListener(), kb_controller]
    for listener in event_listeners:
        EventHandler.register(listener)
        
    run = True
    clock = pygame.time.Clock()
    
    while run:
        clock.tick(configs.FPS)
        
        win.blit(track, (0,0))
        
        car.move()
        print(car.check_collision(track))
        car.draw(win)
        
        pygame.display.update()

        
        for event in pygame.event.get():
            EventHandler.notify(event)
                
    pygame.quit()
                
        
        
        
        
                
        