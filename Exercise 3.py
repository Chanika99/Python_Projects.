#Exercise 03
#Part 1
def check_zander_size():
    size_limit = 42
    length = float(input("Enter the length of the zander in centimeters: "))
    if length >= size_limit:
        print("The zander meets the size limit. You can keep the fish.")
    else:
        shortfall = size_limit - length
        print(f"The zander is {shortfall:.2f} centimeters below the size limit. Please release it back into the lake.")
check_zander_size()
#Part 2
def describe_cabin():
   cabin_class = input("Enter the cabin class (LUX,A,B,C): ").upper()
   if cabin_class == "LUX":
       print ("LUX: upper-deck cabin with a balcony.")
    elif cabin_class == "A":
       print ("A: above the car deck, equipped with a window.")
    elif cabin_class == "B":
       print ("B: windowless cabin above the car deck.")
    elif cabin_class == "C":
        print ("C: windowless cabin below the car deck.")
    else:
        print ("Invalid cabin class.")
describe_cabin()
#Part 3
def check_hemoglobin():
    gender = input("Enter your biological gender (male/female): ").lower()
    hemoglobin_value = float(input("Enter your hemoglobin value (g/l): "))
    if gender == "female":
        if hemoglobin_value < 117:
            print("Your hemoglobin value is low.")
        elif 117 <= hemoglobin_value <= 155:
            print("Your hemoglobin value is normal.")
        else:
            print("Your hemoglobin value is high.")
    elif gender == "male":
        if hemoglobin_value < 134:
            print("Your hemoglobin value is low.")
        elif 134 <= hemoglobin_value <= 167:
            print("Your hemoglobin value is normal.")
        else:
            print("Your hemoglobin value is high.")
    else:
        print("Invalid gender entered. Please enter 'male' or 'female'.")
check_hemoglobin()
#Part 4
def check_leap_year():
    year = int(input("Enter a year: "))
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")
check_leap_year()
