import pygame
import math

import configs

from car import Car
from sensor import Sensor

class SensoredCar(Car):
    
    def __init__(self, image, controller, track):
        super(SensoredCar, self).__init__(image, controller, track)
        
        self.sensors_angles = configs.SENSOR_ANGLES
        self.sensors = self.create_sensors()
        self.sensor_values = [0 for i in range(len(self.sensors_angles))]
    
    def create_sensors(self):
        sensors = []
        for sensor_angle in self.sensors_angles:
            sensors.append(
                Sensor(self, sensor_angle)
            )
        return sensors
    
    def update(self, win):
        super(SensoredCar, self).update(win)
        self.draw(win)
        
        for i, sensor in enumerate(self.sensors):
            sensor.update(win)
            self.sensor_values[i] = sensor.sensor_value
        # print(self.sensor_values)
    
    def draw(self, win):
        super(SensoredCar, self).draw(win)
        