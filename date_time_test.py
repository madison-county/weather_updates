import datetime
# date_time = time.strftime('%m%d%Y%H%M')

current_day = datetime.datetime.now()

print(type(current_day))
print(current_day)
#date_split = current_day.split(' ')
#print(date_split)

print(current_day.strftime('%m%d%Y%H%M'))
print(current_day.strftime('%Y/%d/%m-%H:%M'))
date_str = current_day.strftime('%Y/%d/%m-%H:%M')
print(type(date_str))
print(date_str)

locations = {
    "alder" : "45.3238072222328, -112.10734772283459",
    "laurin" : "45.35271239238317, -112.1177774887102",
    "sheridan" : "45.45534588182824, -112.19707886464111",
    "twin bridges" : "45.54419121141109, -112.33107814032275",
    "gravelly range" : "44.92049066357555, -111.83308887669405"
}

for val in locations.items():
   print(val)

#loc_entry = input("Enter a location: \n")
#print("You entered %s" % loc_entry)

valid_input = False
while not valid_input:
    loc_entry = input("Enter a location: \n")
    if loc_entry.lower() in locations:
        print("{0} found in the dictionary".format(loc_entry.upper()))
        valid_input = True
    else:
        print("Error - Locations not found")

#for i in range(len(locations)):
#    for key, val in locations[i].items():
#        print("{0} : {1}".format(key, str(val)))