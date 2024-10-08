import math

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
    "tobacco roots" : "45.5741139791977, -112.00369955681968"
}

def coordinate_trunc(coord_list):
    tmp = coord_list[0]
    latitude = tmp[:7]
    tmp = coord_list[1]
    longitude = tmp[:9]
    return latitude, longitude

#loc_entry = input("Enter a location: \n")
#print("You entered %s" % loc_entry)
def main():
    manual_prompt = input("Would you like to enter coordinates or search for a town? \nPress 1 to search via Latitude/Longitude coordinates.\nPress 2 for searching saved locations.\n")
    match manual_prompt:
        case '1':
            # Get user input for coordinates and send request to weather API
            pass
        case '2':
            print('Case 2')
            valid_input = False
            while not valid_input:
                loc_entry = input("Enter a location ----- Type help or h for a list of locations\n").strip(" ")
                if loc_entry.lower() in locations:
                    print("{0} --- Coordinates: {1}".format(loc_entry.capitalize(), locations[loc_entry]))
                    current_coords = locations[loc_entry].split(', ')
                    latitude, longitude = coordinate_trunc(current_coords)
                    print(type(latitude), latitude, type(longitude), longitude)
                    valid_input = True
                elif loc_entry.lower() == "help" or "h":
                    for key in locations:
                        print(key.capitalize())
                else:
                    print("Error - Location not found")

    #for i in range(len(locations)):
    #    for key, val in locations[i].items():
    #        print("{0} : {1}".format(key, str(val)))

if __name__ == "__main__":
    main()