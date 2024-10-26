from car import Car

car = Car("ABC-123", 142)

print(f"Registration Number: {car.registration_number}")
print(f"Max Speed: {car.max_speed} km/h")
print(f"Current Speed: {car.current_speed} km/h")
print(f"Travelled Distance: {car.travelled_distance} km")

#Accelerate the cai in different speed changes
car.accelerate(30)
car.accelerate(70)
car.accelerate(50)

print(f"Current speed after acceleration: {car.current_speed} km/h")

#Use emergency brake in -200 km/h
car.accelerate(-200)

#Print final speed
print(f"Final speed after emergency brake: {car.current_speed} km/h")