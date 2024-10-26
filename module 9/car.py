import random
class Car:
    def __init__(self,registration_number,max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self,speed_change):
        self.current_speed = self.current_speed + speed_change
        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed
        if self.current_speed < 0:
            self.current_speed = 0

    def drive(self,hours):
        self.travelled_distance = self.travelled_distance + self.current_speed * hours


