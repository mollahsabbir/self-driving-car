import pygame
import numpy as np
from eventhandler import EventHandler

class KeyboardController:
    def __init__(self):
        self.controls_dict = {
            "forward":False,
            "reverse":False,
            "left":False,
            "right":False
        }
        
    def update(self, win, **kargs):
        pass
    
    def listen(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.controls_dict['forward'] = True
            if event.key == pygame.K_DOWN:
                self.controls_dict['reverse'] = True
            if event.key == pygame.K_LEFT:
                self.controls_dict['left'] = True
            if event.key == pygame.K_RIGHT:
                self.controls_dict['right'] = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                self.controls_dict['forward'] = False
            if event.key == pygame.K_DOWN:
                self.controls_dict['reverse'] = False
            if event.key == pygame.K_LEFT:
                self.controls_dict['left'] = False
            if event.key == pygame.K_RIGHT:
                self.controls_dict['right'] = False
                    
    def __getitem__(self, idx):
        return self.controls_dict[idx]

class NNController:
    INDEX_TO_CONTROL = {
        0:"forward",
        1:"reverse",
        2:"right",
        3:"left"
    }
    def __init__(self, neural_net):
        
        self.neural_net = neural_net
        
        self.controls_dict = {
            "forward":False,
            "reverse":False,
            "left":False,
            "right":False
        }
    
    def update(self, win, **kargs):
        sensor_values = kargs['sensor_values']
        
        # Shape shoud be [input, 1]
        values_np = np.array(sensor_values).reshape(-1, 1)
        output = self.neural_net.forward(values_np)
        
        index = np.argmax(output)
        control = NNController.INDEX_TO_CONTROL[index]
        self.controls_dict = {
            "forward":False,
            "reverse":False,
            "left":False,
            "right":False
        }
        self.controls_dict[control] = True
        # print(output)
    
    def __getitem__(self, idx):
        return self.controls_dict[idx]