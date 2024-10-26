import random
from car import Car

cars = []
for i in range(10):
    max_speed = random.randint(100,200)
    registration_number = f'ABC-{i+1}'
    cars.append(Car(registration_number,max_speed))

#start the race
race_finished = False
while not race_finished:
    for car in cars:
        speed_change = random.randint(-10,15) #random speed
        car.accelerate(speed_change)

        car.drive(1)

        if car.travelled_distance >= 10000:
            race_finished = True
            break

print \
    (f"{'Registration':<12} | {'Max speed (km/h)':<15} | {'Current speed (km/h)':<20} | {'Travelled distance (km)':<20}")
print("-"*65)
for car in cars:
    print \
        (f"{car.registration_number:<12} | {car.max_speed:<15} | {car.current_speed:<20} | {car.travelled_distance}")

