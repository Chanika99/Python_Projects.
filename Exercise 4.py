import random
import math
#Part 1
def print_divisible_by_three():
    number = 1

    while number <= 1000:
        if number % 3 == 0:
            print(number)
        number += 1
print_divisible_by_three()
#Part 2
def inches_to_cm():
    print("This program converts inches to centimeters.")
    print("Enter a negative value to quit.")

    while True:
        try:
            inches = float(input("Enter the value in inches: "))

            if inches < 0:
                print("Negative value entered. Exiting the program.")
                break

            centimeters = inches * 2.54
            print(f"{inches} inches is equal to {centimeters} centimeters.")

        except ValueError:
            print("Please enter a valid number.")
inches_to_cm()
#Part 3
def find_min_max():
    numbers = []
    print("Enter numbers one by one. Press Enter on an empty line to stop.")
    while True:
        user_input = input("Enter a number: ")

        if user_input == "":
            break

        try:
            number = float(user_input)
            numbers.append(number)
        except ValueError:
            print("That's not a valid number. Please try again.")

    if numbers:
        smallest = min(numbers)
        largest = max(numbers)
        print(f"The smallest number you entered is: {smallest}")
        print(f"The largest number you entered is: {largest}")
    else:
        print("No numbers were entered.")
find_min_max()
#Part 4
def guessing_numbers_game():
    number = random.randint(1, 10)
    print ("Welcome to the Guessing Game!")
    print ("I have drawn a random number between 1 and 10.")

    while True:
        guess = int(input("Please enter your guess: "))
        if guess < number:
            print("Too low.")
        elif guess > number:
            print("Too high.")
        else:
            print("Correct! You guessed the right number!")
            break
guessing_numbers_game()

#Part 5
username = "python"
password = "rules"
num_try = 5
while num_try > 0:
    name = input("Enter your username: ")
    pas = input("Enter your password: ")
    if name == username and pas == password:
        print("Welcome!")
        break

    num_try = num_try - 1
else:
    print("Access denied")
#part 6


random_points = int(input("how many random points to be generated? "))
n = 0
i = 0
while i < random_points:
    x = random.uniform(-1, 1.)
    y = random.uniform(-1, 1.)
    if x**2 + y**2 <= 1:
        n +=1

    i += 1
pi = 4 * n / random_points
print(f"Pi estimation is {pi},the difference with math pi is:{math.pi - pi}")