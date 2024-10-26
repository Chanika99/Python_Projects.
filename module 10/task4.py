import random
from tabulate import tabulate

class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, speed_change):
        self.current_speed += speed_change
        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed
        elif self.current_speed < 0:
            self.current_speed = 0

    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours

class Race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars

    def hour_passes(self):
        for car in self.cars:
            speed_change = random.randint(-10, 15)
            car.accelerate(speed_change)
            car.drive(1)

    def print_status(self):
        headers = ["Registration", "Max Speed (km/h)", "Current Speed (km/h)", "Travelled Distance (km)"]
        car_data = [
            [car.registration_number, car.max_speed, car.current_speed, f"{car.travelled_distance:.1f}"]
            for car in self.cars
        ]
        print(tabulate(car_data, headers=headers, tablefmt="grid"))

    def race_finished(self):
        return any(car.travelled_distance >= self.distance for car in self.cars)

# Main program
cars = []
for i in range(1, 11):
    max_speed = random.randint(100, 200)
    registration_number = f"ABC-{i}"
    cars.append(Car(registration_number, max_speed))

race = Race("Grand Demolition Derby", 8000, cars)

hours = 0
while not race.race_finished():
    race.hour_passes()
    hours += 1

    if hours % 10 == 0:
        print(f"\nRace status at hour {hours}:")
        race.print_status()

print("\nRace finished!")
race.print_status()
