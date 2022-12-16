# Lists with dictionary parsing:
# https://www.geeksforgeeks.org/iterate-through-list-of-dictionaries-in-python/

import requests
import json
import datetime
from datetime import date
import os
from fpdf import FPDF

locations = {
    "alder" : "45.3238072222328, -112.10734772283459",
    "laurin" : "45.35271239238317, -112.1177774887102",
    "sheridan" : "45.45534588182824, -112.19707886464111",
    "twin bridges" : "45.54419121141109, -112.33107814032275",
    "virginia city" : "45.29428905204298, -111.9402042591855",
    "pony" : "45.658636620177, -111.89338788673528",
    "ennis" : "45.34909074316909, -111.73103034191642",
    "mcallister" : "45.44484117129293, -111.73200254488343",
    "gravelly range" : "44.92049066357555, -111.83308887669405",
    "tobacco roots" : "45.5741139791977, -112.00369955681968",
    "sar" : "45.65554, -112.69617"
}

def main():
    mission_name = input("Enter a mission name: \n")
    latitude, longitude = user_entry_prompt()

    print("Creating a 7 day forecast for {0} at coordinates {1}, {2}".format(mission_name, latitude, longitude))
    current_day = datetime.datetime.today().strftime('%Y-%m-%d-%H%M')

    coord_url = ("https://api.weather.gov/points/{0},{1}").format(latitude, longitude)

    weather_request = requests.get(coord_url)
    weather_json = json.loads(weather_request.text)
    weather_properties = weather_json.get('properties')

    gridId = weather_properties['gridId']
    gridX = weather_properties['gridX']
    gridY = weather_properties['gridY']
    rel_loc = weather_properties['relativeLocation']
    rel_loc_prop = rel_loc['properties']
    city = rel_loc_prop['city']
    state = rel_loc_prop['state']

    f = open("{0}_{1}_{2}_forecast.txt".format(mission_name, current_day, city.replace(" ", "-")), "w+")

    print(type(weather_properties))
    for key, val in weather_properties.items():
        print("{} : {}".format(key, val))

    grid_properties = grid_request(gridId, gridX, gridY)
    
    print("*******GROND PROPERTIES: ******")
    for item in grid_properties:
        print(grid_properties[item])

    grid_periods = grid_properties['periods']
    print("grid_periods type: ", type(grid_periods))
    print("Length of grid_periods: ", len(grid_periods))

    out_string = str("Latitude: {0}, Longitude: {1}\nWeather Report Created at: {2}.\n{3}, {4}.\nGridId: {5} || GridX: {6} || GridY: {7}\n\n".format(
        latitude, longitude, current_day, city, state, gridId, gridX, gridY))

    write_out(f, out_string, grid_periods)

def coordinate_trunc(coord_list):
    if type(coord_list) == list:
        print("***** {0} found *****".format(type(coord_list)))
        tmp = coord_list[0]
        latitude = tmp[:7]
        tmp = coord_list[1]
        longitude = tmp[:9]
    return latitude, longitude

def write_out(file, string, grid_periods):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size = 10)

    file.write(string)
    pdf.multi_cell(200, 4, txt=string, align="C")

    for i in range(len(grid_periods)):
        #print('\n')
        for key, val in grid_periods[i].items():
            #print("{} : {}".format(key, val))
            file.write("{0} : {1} \n".format(key, str(val)))
            pdf.multi_cell(200, 4, txt = "{0} : {1}".format(key, str(val)), align="L")
        pdf.cell(200, 10, txt="")

    pdf.output("%s.pdf" % file.name.replace('.txt', ""))
    file.close()

def grid_request(gridId, gridX, gridY):
    valid_request = False
    while not valid_request:
        try :
            print("Pinging Weather API with: {0}, {1}, {2}.".format(gridId, gridX, gridY))
            grid_request = ("https://api.weather.gov/gridpoints/{0}/{1},{2}/forecast").format(gridId, gridX, gridY)
            grid_request = requests.get(grid_request)
            if grid_request.status_code == 500:
                print("Response code 500 -------- Pinging server again")
                grid_request = requests.get(grid_request)
            grid_json = json.loads(grid_request.text)
            grid_properties = grid_json.get('properties')
            valid_request = True
            print("Request C/W", type(grid_properties))
        except ConnectionError as err:
            print("Request error: %s" % err)
        except Exception as err:
            print("Another error: %s" % err)
    return grid_properties

def user_entry_prompt():
    manual_prompt = input("Would you like to enter coordinates or search for a town? \nPress 1 to search via Latitude/Longitude coordinates.\nPress 2 for searching saved locations.\n")
    match manual_prompt:
        case '1':
            latitude = input("Enter the desired latitude: \n")
            longitude = input("Enter the desired longitude: \n")
            #current_coords = input("Enter Latitude, Longitude --- Example: 45.2435, -112.54345\n")
            #print(type(current_coords), current_coords)
            #latitude, longitude = coordinate_trunc(current_coords)
        case '2':
            valid_input = False
            while not valid_input:
                loc_entry = input("Enter a location ----- Type help or h for a list of locations\n").strip(" ").lower()
                if loc_entry in locations:
                    #print("{0} --- Coordinates: {1}".format(loc_entry.capitalize(), locations[loc_entry]))
                    current_coords = locations[loc_entry].split(', ')
                    latitude, longitude = coordinate_trunc(current_coords)
                    #print(type(latitude), latitude, type(longitude), longitude)
                    valid_input = True
                elif loc_entry.lower() == "help" or "h":
                    for key in locations:
                        print(key.capitalize())
                else:
                    print("Error - Location not found")
    return latitude, longitude

if __name__ == "__main__":
    main()