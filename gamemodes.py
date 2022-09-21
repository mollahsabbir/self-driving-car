import pygame
import configs
import math
import pickle

from car import Car
from sensoredcar import SensoredCar
from controllers import KeyboardController, NNController
from eventhandler import EventHandler, GameExitEventListener

from network import Network, NetworkFactory

'''
============================================================
'''
class KeyboardGameMode:
    def play(self):
        track = pygame.image.load(configs.TRACK_IMAGE)
        car_image = pygame.image.load(configs.CAR_IMAGE)
        
        kb_controller = KeyboardController()
        car = Car(car_image, kb_controller, track)
        
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
            car.update(win)
            pygame.display.update()
            
            for event in pygame.event.get():
                EventHandler.notify(event)
                    
        pygame.quit()


'''
============================================================
'''

 
class TrainGameMode:
    def __init__(self):
        self.num_cars = configs.TRAIN_CARS_NUMBER
        self.track = pygame.image.load(configs.TRACK_IMAGE)
        
        self.cars = self.create_new_cars()
        
    def create_new_cars(self):
        cars = []
        network_factory = NetworkFactory(configs.NN_LAYERS_DIMS)
        networks = network_factory.create_mutated_networks(self.num_cars)
        
        for i in range(self.num_cars):
            car_image = pygame.image.load(configs.CAR_IMAGE)
            nn_controller = NNController(networks[i])
            cars.append(
                SensoredCar(car_image, nn_controller, self.track)
            )
        return cars
    
    def create_cars_from_best(self):
        cars = []
        with open(configs.MODEL_LOCATION, 'rb') as handle:
            best_network = pickle.load(handle)
        network_factory = NetworkFactory(configs.NN_LAYERS_DIMS)
        networks = network_factory.create_mutated_networks(self.num_cars, best_network)
        
        for i in range(self.num_cars):
            car_image = pygame.image.load(configs.CAR_IMAGE)
            nn_controller = NNController(networks[i])
            cars.append(
                SensoredCar(car_image, nn_controller, self.track)
            )
        return cars
    
    def save_best_car_model(self):
        save_location = configs.MODEL_LOCATION
        
        best_car = max(self.cars, key=lambda x: x.score)
        best_network = best_car.controller.neural_net
        
        with open(save_location, 'wb') as handle:
            pickle.dump(best_network, handle, protocol=pickle.HIGHEST_PROTOCOL)
    
    def play(self):
          
        win_width, win_height = (self.track.get_width(), 
                                self.track.get_height())
        win = pygame.display.set_mode((win_width, win_height))
        pygame.display.set_caption("Self Driving Car")
        
        event_listeners = [GameExitEventListener()]
        for listener in event_listeners:
            EventHandler.register(listener)
            
        clock = pygame.time.Clock()
        
        pygame.font.init()
        font = pygame.font.Font(pygame.font.get_default_font(), 25)
        
        pygame.time.set_timer(pygame.USEREVENT, 1000)
        
        run = True
        generation = 1
        counter = configs.SECONDS_PER_GENERATION
        while run:
            clock.tick(configs.FPS)
            win.blit(self.track, (0,0))
            
            all_cars_stopped = all([abs(car.speed)<0.3 for car in self.cars])
            time_to_check = counter%10==0 and counter != configs.SECONDS_PER_GENERATION
            
            if (time_to_check and all_cars_stopped) or counter==0:
                generation += 1
                counter = configs.SECONDS_PER_GENERATION
                self.save_best_car_model()
                self.cars = self.create_cars_from_best()
            
            text_surface = font.render('Generation: ' + str(generation),True,(0, 0, 0))
            win.blit(text_surface, dest=(5,5))
            text_surface = font.render('Time: ' + str(counter),True,(0, 0, 0))
            win.blit(text_surface, dest=(5,35))
            
            for car in self.cars:
                car.update(win)
                
            pygame.display.update()
            
            for event in pygame.event.get():
                EventHandler.notify(event)
                if event.type == pygame.USEREVENT: 
                        counter -= 1
                    
        pygame.quit()
 
 
'''
============================================================
'''       
class SelfDrivingGameMode:
    def play(self):
        track = pygame.image.load(configs.TRACK_IMAGE)
        car_image = pygame.image.load(configs.CAR_IMAGE)
             
        with open(configs.MODEL_LOCATION, 'rb') as handle:
            best_network = pickle.load(handle)
            
        nn_controller = NNController(best_network)
        car = SensoredCar(car_image, nn_controller, track)
        
        win_width, win_height = track.get_width(), track.get_height()
        win = pygame.display.set_mode((win_width, win_height))
        pygame.display.set_caption("Self Driving Car")
        
        event_listeners = [GameExitEventListener()]
        for listener in event_listeners:
            EventHandler.register(listener)
            
        run = True
        clock = pygame.time.Clock()
        
        while run:
            clock.tick(configs.FPS)
            win.blit(track, (0,0))
            car.update(win)
            pygame.display.update()
            
            for event in pygame.event.get():
                EventHandler.notify(event)
                    
        pygame.quit()