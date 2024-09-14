# Exercise 1

import mysql.connector
from mysql.connector import Error

def get_airport_details(icao_code):
    try:

        connection = mysql.connector.connect(
            host='localhost',
            database='flight_game',
            user='root',
            password='Chani@0514'
        )

        if connection.is_connected():
            cursor = connection.cursor()

            query = "SELECT name, municipality FROM airport WHERE ident = %s"
            cursor.execute(query, (icao_code,))
            result = cursor.fetchone()

            if result:
                print(f"Airport Name: {result[0]}")
                print(f"Location (Town): {result[1]}")
            else:
                print(f"No airport found for ICAO code: {icao_code}")

    except Error as e:
        print(f"Error while connecting to MySQL: {e}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection closed.")

if __name__ == "__main__":
    icao_code = input("Enter the ICAO code of the airport: ").upper()
    get_airport_details(icao_code)
    

# Exercise 2

def get_airports_by_country_code(country_code):

    sql = f"SELECT type, COUNT(*) AS count FROM airport WHERE iso_country = '{country_code}' GROUP BY type ORDER BY count DESC"
    cursor = connection.cursor()
    cursor.execute(sql)
    results = cursor.fetchall()

    if results:
        print(f"Airports in country code '{country_code}':")
        for row in results:
            airport_type, count = row
            print(f"{count} {airport_type} airports")
    else:
        print(f"No airports found for country code: {country_code}")

if _name_ == "_main_":
    country_code = input("Enter the country code (e.g., FI for Finland): ").upper()
    get_airports_by_country_code(country_code)

connection.close()

# Exercise 3
import mysql.connector
from geopy.distance import great_circle

connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='root',
    password='Chani@0514',
    autocommit=True
)
def get_airport_coordinates(icao):
    sql = f"SELECT latitude_deg, longitude_deg FROM airport WHERE ident = '{icao}'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchone()
    return result

def calculate_distance(icao1, icao2):
    coord1 = get_airport_coordinates(icao1)
    coord2 = get_airport_coordinates(icao2)

    if coord1 and coord2:
        distance = great_circle(coord1, coord2).kilometers
        print(f"The distance between {icao1} and {icao2} is {distance:.2f} kilometers.")
    else:
        print("One or both ICAO codes are invalid or not found in the database.")

    if name == "_main_":
       icao_code1 = input("Enter the ICAO code of the first airport: ").upper()
       icao_code2 = input("Enter the ICAO code of the second airport: ").upper()
    calculate_distance(icao_code1, icao_code2)

connection.close()

