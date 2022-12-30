# Weather Forecasting Updates Based on Latitude & Longitude Coordinates

## Language and version: 
* Python - 3.10.6

## Installed Packages:
* `requests`
* `json`
* `os`
* `datetime`
* `time`

## Scope and Overview:
* The scope of the program is to return a 7 day weather forecast from a given set of latitude and longitude corrdinates. 
* These coordinates can be supplied manually during runtime, or indexed via stored locations within a dictionary.
* The information returned from the API is then written into a `.pdf` file with a
respective image for each subsequent day.

## Program Pathing and Environments:

## External API:
* `api.weather.gov` is currently the only API being utilized  

### Running the program:
* Running from a CLI is as followed:
    * `p3 grid_requests.py`
    * This will prompt the user to enter a name for the `pdf` output.
    * Next, the user will enter `1` to enter latitude/longitude manually, or enter `2` to used a saved location within the program's dictionary
        * It is possible to type `help` after entering `2` to show a list of potential locations to return a forecast.

### Common Problems and Troubleshooting:

### Additional Comments