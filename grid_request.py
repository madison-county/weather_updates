# Lists with dictionary parsing:
# https://www.geeksforgeeks.org/iterate-through-list-of-dictionaries-in-python/

import requests
import json
import datetime
import os
import time
from datetime import date
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

    print(f'Creating a 7 day forecast for {mission_name} at coordinates {latitude}, {longitude}')
    current_day = datetime.datetime.today().strftime('%Y-%m-%d-%H%M')

    weather_properties = coordinate_request(latitude, longitude)
    gridId, gridX, gridY, rel_loc, rel_loc_prop, city, state = get_grid_fields(weather_properties)

    print(f'Returning forecast for {city}, {state}')

    f = open(f'{mission_name}_{current_day}_{city.replace(" ", "-")}_forecast.txt', 'w+')

    grid_properties = grid_request(gridId, gridX, gridY)

    for item in grid_properties:
        print(f'***** Grid Properties: {grid_properties[item]} *****\n')

    grid_periods = grid_properties['periods']
    print("grid_periods type: ", type(grid_periods))
    print("Length of grid_periods: ", len(grid_periods))

    out_string = str(f'Latitude: {latitude}, Longitude: {longitude}\nWeather Report Created at: {current_day}.\n{city}, {state}.\nGridId: {gridId} || GridX: {gridX} || GridY: {gridY}\n\n')

    write_out(f, out_string, grid_periods)

def coordinate_trunc(coord_list):
    if type(coord_list) == list:
        print(f'***** {type(coord_list)} found *****')
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
        for key, val in grid_periods[i].items():
            file.write("{0} : {1} \n".format(key, str(val)))
            if key == "icon":
                # ??? it works
                pdf.image("{}#.PNG".format(val))
            elif type(val) == dict:
                print(val["value"])
                pdf.multi_cell(200, 4, txt=f'{key} : {val["value"]}', align="L")
            else:
                pdf.multi_cell(200, 4, txt = f'{key} : {str(val)}', align="L")
        pdf.cell(200, 10, txt="")

    pdf.output("%s.pdf" % file.name.replace('.txt', ""))
    file.close()

def grid_request(gridId, gridX, gridY):
    valid_request = False
    while not valid_request:
        try :
            print(f'Pinging Weather API with: {gridId}, {gridX}, {gridY}.')
            grid_request = (f'https://api.weather.gov/gridpoints/{gridId}/{gridX},{gridY}/forecast')
            grid_request = requests.get(grid_request)
            print(f'*** Return Status {grid_request.status_code} ***')
            match grid_request.status_code:
                case [500, 503]:
                    print("Server Error -------- Pinging server again")
                    grid_request = requests.get(grid_request)
                    time.sleep(15)
                case 200:
                    grid_json = json.loads(grid_request.text)
                    grid_properties = grid_json.get('properties')
                    valid_request = True
                    print("Request C/W", type(grid_properties))
        except ConnectionError as err:
            print(f'Request error: {err}')
        except Exception as err:
            print(f'Server error code: {err}')
    return grid_properties

def coordinate_request(latitude, longitude):
    coord_url = (f'https://api.weather.gov/points/{latitude},{longitude}')

    weather_request = requests.get(coord_url)
    weather_json = json.loads(weather_request.text)
    weather_properties = weather_json.get('properties')

    return weather_properties

def get_grid_fields(weather_properties):
    gridId = weather_properties['gridId']
    gridX = weather_properties['gridX']
    gridY = weather_properties['gridY']
    rel_loc = weather_properties['relativeLocation']
    rel_loc_prop = rel_loc['properties']
    city = rel_loc_prop['city']
    state = rel_loc_prop['state']

    return gridId, gridX, gridY, rel_loc, rel_loc_prop, city, state

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