import pygame
import sys
import time
import math
import configs

from car import Car
from sensoredcar import SensoredCar
from controllers import KeyboardController
from eventhandler import EventHandler, GameExitEventListener

from gamemodes import KeyboardGameMode, TrainGameMode, SelfDrivingGameMode

if __name__ == "__main__":
    
    if configs.GAME_MODE == "TRAIN":
        game_mode = TrainGameMode()
    elif configs.GAME_MODE == "SELFDRIVING":
        game_mode = SelfDrivingGameMode()
    else:
        game_mode = KeyboardGameMode()
    
    game_mode.play()
                
        
        
        
        
                
        