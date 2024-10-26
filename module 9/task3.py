from car import Car

car = Car("ABC-123", 142)

print(f'''
Registration Number: {car.registration_number}
Max Speed: {car.max_speed} km/h
Current Speed: {car.current_speed} km/h
Travelled Distance: {car.travelled_distance} km
'''
      )


#Accelerate the cai in different speed changes
car.accelerate(30)
car.accelerate(70)
car.accelerate(50)

print(f"Current speed after acceleration: {car.current_speed} km/h")

#use drive method for 1.5 hours
car.drive(1.5)

print(f'Travelled Distance after driving for 1.5 hours: {car.travelled_distance} km')

#Use emergency brake in -200 km/h
car.accelerate(-200)

#Print final speed and travelled distance
print(f"Final speed after emergency brake: {car.current_speed} km/h")
print(f'Final Travelled distance: {car.travelled_distance} km')






