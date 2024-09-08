import random

#Excercise 01
num_dice = int(input("How many dice would you like to roll? "))

total = 0

for _ in range(num_dice):
    roll = random.randint(1, 6)
    print(f"Rolled: {roll}")
    total += roll
print(f"Total sum of the dice rolls: {total}")

#Excercise 02
numbers = []

while True:
    user_input = input("Enter a number (or press Enter to quit): ")

    if user_input == "":
        break
    try:
        number = float(user_input)
        numbers.append(number)
    except ValueError:
        print("Please enter a valid number.")

numbers.sort(reverse=True)
top_five = numbers[:5]
print(f"The five greatest numbers are: {top_five}")

#Excercise 03
# Function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False  # If divisible by any number other than 1 and itself, it's not prime
    return True

num = int(input("Enter an integer: "))
if is_prime(num):
    print(f"{num} is a prime number. It can only be divided by 1 and {num}.")
else:
    print(f"{num} is not a prime number. It is divisible by other numbers besides 1 and {num}.")

#Excercise 04
cities = []

for i in range(5):
    city = input(f"Enter the name of city {i+1}: ")
    cities.append(city)

print("\nThe cities you entered are:")
for city in cities:
    print(city)







