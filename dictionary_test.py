locations = {
    "alder" : "45.3238072222328, -112.10734772283459",
    "laurin" : "45.35271239238317, -112.1177774887102",
    "sheridan" : "45.45534588182824, -112.19707886464111",
    "twin bridges" : "45.54419121141109, -112.33107814032275",
    "gravelly range" : "44.92049066357555, -111.83308887669405"
}

#loc_entry = input("Enter a location: \n")
#print("You entered %s" % loc_entry)

valid_input = False
while not valid_input:
    loc_entry = input("Enter a location or type help for a list of locations ----- ")
    if loc_entry.lower() in locations:
        print("{0} --- Coordinates: {1}".format(loc_entry.capitalize(), locations[loc_entry]))
        valid_input = True
    elif loc_entry == "help":
        for key in locations:
            print(key.capitalize())
    else:
        print("Error - Location not found")

#for i in range(len(locations)):
#    for key, val in locations[i].items():
#        print("{0} : {1}".format(key, str(val)))