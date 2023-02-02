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
respective weather image for each subsequent day.

## Program Pathing and Environments:

## External API:
* `api.weather.gov` is currently the only API being utilized  
* https://www.weather.gov/documentation/services-web-api

### Running the program:
* Running from a CLI is as followed:
    * `p3 grid_requests.py`
    * This will prompt the user to enter a name for the `pdf` output (mission name).
    * Standard output format is `mission name_YYYY-MM-DD-HHMM_Location_forecast`
        * Example: `example_2022-12-30-1505_Virginia-City_forecast`
    * Next, the user will enter `1` to enter latitude/longitude manually, or enter `2` to used a saved location within the program's dictionary
        * It is possible to type `help` after entering `2` to show a list of potential locations to return a forecast.
    * Error handling is included for `500` or `503` error responses from the server.
        * Additionally, it is documented on their site that the server occasionally return `500` errors, which can be negated by re-sending the request.
        * If a response code of `500` or `503` is returned, the program will wait 15 seconds before sending another requests and continue to do so until the request is successful.
            * `Known Issues` can be found from the API link above, under the `Updates` tab.
        * Interupting this loop can be achieved by `Ctrl+C` or `Ctrl+D` via the CLI.

### Common Problems and Troubleshooting:

### Additional Comments
* `example_2022-12-30-1505_Virginia-City_forecast` is an example of program output
* Weather Stations listings:
    * https://www.weather.gov/NWR/stations?State=MT
* MT Weather Station Codes (Not updated on the aforementioned link):
    * Billings: `KBLX`
    * Great Falls: `KTFX`
    * Glasgow: `KGGW`
    * Missoula: `KMSX`