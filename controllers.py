import pygame
from eventhandler import EventHandler

class KeyboardController:
    def __init__(self):
        self.controls_dict = {
            "forward":False,
            "reverse":False,
            "left":False,
            "right":False
        }
        
    # @EventHandler.register(pygame.KEYDOWN)
    # def keydownPrint(self, event):
    #     print(event.key)
        
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
    