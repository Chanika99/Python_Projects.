import random

#Excersise 1
def dice_roll():
    return random.randint(1, 6)

while True:
    dice = dice_roll()
    print(f"dices eyes are :{dice}")
    if dice == 6:
        break

#Excercise 2

def roll_dice(sides):
    return random.randint(1, sides)

def main():
    sides = int(input("Enter the number of sides on the dice: "))

    roll = 0

    while roll != sides:
        roll = roll_dice(sides)
        print(f"Rolled: {roll}")

    print(f"Max number {sides} rolled! Program ended.")

if __name__ == "__main__":
    main()

#Excercise 3
GALLON_TO_LITRE = 3.78541
def gallons_to_liters(gallons):

    return gallons * GALLON_TO_LITRE

def main():
    while True:
        gallons = float(input("Enter the quantity of gasoline in gallons (negative to quit): "))

        if gallons < 0:
            print("Negative value entered. Program ended.")
            break

        liters = gallons_to_liters(gallons)

        print(f"{gallons} gallons is equal to {liters:.2f} liters.\n")

if __name__ == "__main__":
    main()

#EX4
def sum(num_list):
    total_sum = 0
    for i in num_list:
        total_sum += i
    return total_sum

ex_list = []
for number in range(10):
    ex_list.append(random.randint(1, 10))
    print(f"The list of numbers is: ")

    for i in range (len(ex_list)):
        print(ex_list[i],end= " ")

    print (f"\nThe sum of all items in the list is:{sum(ex_list)}")

#ex 5
def make_even (num_list):
    result = []
    for i in range (len(num_list))
        if num_list[i]%2 == 0:
            result.append(num_list[i])
    return result
def print_list(message, num_list):
    print(message, end=": ")
    for i in range (len(num_list)):
        print(num_list[i],end=" ")

example_list = []
for n in range(10):
    example_list.append(random.randint(1, 10))
print_list ("Original list", example_list)
new_list = make_even(example_list)
print_list("only even numbers list", new_list)

#Excercise 6
import math

def calculate_unit_price(diameter_cm, price_euros):
    radius_m = (diameter_cm / 2) / 100
    area_m2 = math.pi * radius_m ** 2
    unit_price = price_euros / area_m2
    return unit_price

# Main program
def main():
    diameter1 = float(input("Enter the diameter of the first pizza (in cm): "))
    price1 = float(input("Enter the price of the first pizza (in euros): "))

    diameter2 = float(input("Enter the diameter of the second pizza (in cm): "))
    price2 = float(input("Enter the price of the second pizza (in euros): "))

    unit_price1 = calculate_unit_price(diameter1, price1)
    unit_price2 = calculate_unit_price(diameter2, price2)

    print(f"\nUnit price of first pizza: {unit_price1:.2f} €/m²")
    print(f"Unit price of second pizza: {unit_price2:.2f} €/m²")

    if unit_price1 < unit_price2:
        print("The first pizza provides better value for money.")
    elif unit_price2 < unit_price1:
        print("The second pizza provides better value for money.")
    else:
        print("Both pizzas provide the same value for money.")

if __name__ == "__main__":
    main()

