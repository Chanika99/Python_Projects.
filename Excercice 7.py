##Nape Vithanage Chanika Anjalee
#Assignment 7
#Ex 01

seasons= ("Winter", "Spring", "Summer", "Autumn")
month_of_the_year= int(input("Enter the number of the month (1-12): "))

if month_of_the_year in (12, 1, 2):
    Season= ("Winter")
elif month_of_the_year in (3, 4, 5):
    Season = ("Spring")
elif month_of_the_year in (6, 7, 8):
    Season = ("Summer")
elif month_of_the_year in (9, 10, 11):
    Season = ("Autumn")
else:
    Season = "Invalid month number"

print(f"The seasons is: {Season}")

#EX 02
names_set = set()
while True:
    name = input("Enter a name or (Press enter to finish): ")
    if name == "":
        break
    if name in names_set:
        print("Existing name")
    else:
        print("New name")
        names_set.add(name)

print("\nList of entered names:")
for name in names_set:
        print(name)
#EX 03
airports = {}
while True:
    print("\nMenu: ")
    print("1.Enter a new airport: ")
    print("2.Fetch airport information")
    print("3.Quit")
    choice = input("Choose an option (1-3): ")
    if choice == '1':
        icao_code = input("Enter the ICAO code of the airport: ").upper()
        airport_name = input("Enter the name of the airport: ")
        if icao_code in airports:
            print("This airport already exists.")
        else:
            airports[icao_code] = airport_name
            print(f"Airport {airport_name} added with ICAO code {icao_code}.")

    elif choice == '2':
        icao_code = input("Enter the ICAO code of the airport to fetch: ").upper()

        if icao_code in airports:
            print(f"The name of the airport with ICAO code {icao_code} is {airports[icao_code]}.")
        else:
            print("Airport not found.")

    elif choice == '3':
        print("Exiting the program.")
        break

    else:
        print("Invalid option, please choose 1, 2, or 3.")




