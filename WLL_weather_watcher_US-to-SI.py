#!/usr/bin/python3

#
# Python 3 script to pull weather data from a Davis Instruments
# WeatherLink Live and publish a file for INDI's Weather Watcher to
# monitor.
#

#
# This version is takes US units as inputs and publishes SI units
#

import requests
from datetime import datetime
import time 
import json
import os


# url for outside temperature update x.x.x.x to correct values
current_conditions_url = 'http://x.x.x.x:80/v1/current_conditions'
# file to be monitored by Weather Watcher full path required 
filename = "full_path_to_file"
# update interval
interval = 30


 
while True:

		resp = requests.get(current_conditions_url)
		#print("HTTP Response Code:", resp)
		json_data = json.loads(resp.text)        

		temp = json_data['data'] ['conditions'] [0] ['temp']
		dewpoint = json_data['data'] ['conditions'] [0] ['dew_point']
		humidity = json_data['data'] ['conditions'] [0] ['hum']		
		pressure = json_data['data'] ['conditions'] [2] ['bar_sea_level']
		wind_speed = json_data['data'] ['conditions'] [0] ['wind_speed_avg_last_1_min']
		wind_dir = json_data['data'] ['conditions'] [0] ['wind_dir_scalar_avg_last_1_min']
		rain_rate = float(json_data['data'] ['conditions'] [0] ['rain_rate_last'])/100.0 # 0.01" bucket
			  		
# write current.txt (current conditions for indi)		
		file1 = open(filename, "w")
		d = datetime.utcnow()
		dformatted = "dataGMTTime="+d.strftime("%Y/%m/%d %H:%M:%S")
		file1.write (dformatted + "\n")
		temp_str = "temperature="+ str(round(((temp-32)/1.8), 2)) + "\n"
		file1.write(temp_str)
		temp_str = "Humidity="+ str(humidity) + "\n"
		file1.write(temp_str)
		temp_str = "Wind="+ str(round(wind_speed*1.6, 2)) + "\n"
		file1.write(temp_str)
		temp_str = "Rain=" + str(round(rain_rate*25.4, 2)) + "\n"
		file1.write(temp_str)
		temp_str = "Pressure=" + str(int(pressure*33.8639)) + "\n"
		file1.write(temp_str)
		file1.close()
		
		  
		time.sleep(interval)
