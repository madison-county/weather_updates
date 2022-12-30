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
* https://www.weather.gov/documentation/services-web-api
### Running the program:
* Running from a CLI is as followed:
    * `p3 grid_requests.py`
    * This will prompt the user to enter a name for the `pdf` output.
    * Next, the user will enter `1` to enter latitude/longitude manually, or enter `2` to used a saved location within the program's dictionary
        * It is possible to type `help` after entering `2` to show a list of potential locations to return a forecast.
    * Error handling is included for `500` or `503` error responses from the server.
        * Additionally, it is documented on their site that the server occasionally return `500` errors, which can be negated by re-sending the request.
        * If a response code of `500` or `503` is returned, the program will wait 15 seconds before sending another requests and continue to do so until the request is successful.
        * Interupting this loop can be achieved by `Ctrl+C` or `Ctrl+D` via the CLI.

### Common Problems and Troubleshooting:

### Additional Comments