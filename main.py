import requests
import json

#latitude_input = input("Enter a latitude (Ex: 45.3454564): \n")
#print("You entered: %s" % latitude_input)

#longitude_input = input("Enter a longitude (Ex: -112.653456 ): \n")
#print("You entered: %s" % longitude_input)

latitude = 45.32375898982923
longitude = -112.10761562255259

coord_url = ("https://api.weather.gov/points/{0},{1}").format(latitude, longitude)
print(coord_url)

weather_request = requests.get(coord_url)
weather = weather_request.json()
weather_json = json.loads(weather_request.text)

#print(weather.text)
# Weather is a dictionary
print(type(weather))

#print(weather['gridId'])

# Print the dictionary keys
for key in weather:
    print(key, '->', weather[key], '\n')

print('End for loop\n')

for key in weather.items():
    print(key)
    print(type(key))

print('End for loop\n')

for key, value in weather.items():
    print(key, '->', value)

print('End for loop\n')

weather_keys = weather.keys()
print(weather_keys, '\n')

weather_values = weather.values()
print(weather_values, '\n')

print('id' in weather.keys())
print('county' in weather.values())

print(weather_json.get('properties'))

for item in weather_json.get('properties'):
    print(item)

weather_properties = weather_json.get('properties')

print('gridX' in weather_properties)
print('gridY' in weather_properties)

print('GridID: ', weather_properties['gridId'])
print('GridX: ', weather_properties['gridX'])
print('GridY: ', weather_properties['gridY'])

gridId = weather_properties['gridId']
gridX = weather_properties['gridX']
gridY = weather_properties['gridY']

print(gridId, gridX, gridY)

#print("Context: ", weather['@context'], "\n")
#print("ID: ", weather['id'], "\n")
#print("Geometry: ", weather['geometry'], '\n')
#print("Properties: ", weather['properties'], '\n')

grid_request = ("https://api.weather.gov/gridpoints/{0}/{1},{2}/forecast").format(gridId, gridX, gridY)
