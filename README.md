# WLL_to_Weather_Watcher

These are two different Python 3 scripts each of which can be used to pull data from a Davis WeatherLink Live device 
and write it to a file where INDI's Weather Watcher driver can read the values.

Requirements:

Davis Weather Link Live

INDI
 
Python 3 dependencies
- requests
- datetime
- time
- json
- os

Before use, the user will need to change the lines for the url to the WeatherLink Live, the path and file name for the data and, if desired,
adjust the interval between readings.

If the code does not work, the json for the WeatherLink Live may not be consistent with the unit from which 
the script was prepared.  If this is the case, it is recommended to take the following steps (substituting values as requred):

curl http://ip_wll:80/v1/current_conditions > file.json

open file.json in a browser which will show the json data in an easy to read format (e.g., firefox)

adjust the indices of the json_data statements to match
