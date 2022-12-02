# Lists with dictionary parsing:
# https://www.geeksforgeeks.org/iterate-through-list-of-dictionaries-in-python/

import requests
import json
import datetime
from datetime import date
import os
from fpdf import FPDF

def main():
    mission_name = input("Enter a mission name: \n")
    #latitude = input("Enter the desired latitude: \n")
    #longitude = input("Enter the desired longitude: \n")
    latitude = 44.9056
    longitude = -111.8552
    print("Creating a 7 day forecast for {0} at coordinates {1}, {2}".format(mission_name, latitude, longitude))
    current_day = datetime.datetime.today().strftime('%Y-%m-%d-%H:%M:%S')

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
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size = 10)

    locations = {
        "Alder" : "45.3238072222328, -112.10734772283459",
        "Laurin" : "45.35271239238317, -112.1177774887102",
        "Sheridan" : "45.45534588182824, -112.19707886464111",
        "Twin Bridges" : "45.54419121141109, -112.33107814032275"
    }

    for area in locations:
        print(area)

    #print(rel_loc['properties'])
    #print(type(rel_loc_prop))
    #print(rel_loc_prop)
    #print(rel_loc_prop['city'])

    #print(type(weather_properties))
    #for key, val in weather_properties.items():
    #    print("{} : {}".format(key, val))

    grid_request = ("https://api.weather.gov/gridpoints/{0}/{1},{2}/forecast").format(gridId, gridX, gridY)
    grid_request = requests.get(grid_request)

    grid_json = json.loads(grid_request.text)

    #for key in grid_json:
    #    print(key)

    grid_properties = grid_json.get('properties')

    #for item in grid_properties:
    #    print(grid_properties[item])

    grid_periods = grid_properties['periods']
    print("grid_periods type: ", type(grid_periods))
    print("Length of grid_periods: ", len(grid_periods))

    out_string = str("Latitude: {0}, Longitude: {1}\nWeather Report Created at: {2}.\n{3}, {4}.\nGridId: {5} || GridX: {6} || GridY: {7}\n\n".format(
        latitude, longitude, current_day, city, state, gridId, gridX, gridY))

    f.write(out_string)
    pdf.multi_cell(200, 4, txt=out_string, align="C")
    for i in range(len(grid_periods)):
        #print('\n')
        for key, val in grid_periods[i].items():
            #print("{} : {}".format(key, val))
            f.write("{0} : {1} \n".format(key, str(val)))
            pdf.multi_cell(200, 4, txt = "{0} : {1}".format(key, str(val)), align="L")
        pdf.cell(200, 10, txt="")
        f.write("\n")

    pdf.output("%s.pdf" % f.name.replace('.txt', ""))
    f.close()

    #while True:
    #    print("Enter a forecast to index [0-13] or type 'help' for options: ")
    #    user_entry = input("---- ")
    #    try:
    #        if user_entry == "help":
    #            print("Press <Ctrl + c> to quit")
    #            print("Indexing for weather starts at '0'\n")
    #            continue
    #        print(grid_periods[int(user_entry)])
    #    except Exception as err:
    #        print("error: %s --- Enter a number between 0-13)" % err)

if __name__ == "__main__":
    main()