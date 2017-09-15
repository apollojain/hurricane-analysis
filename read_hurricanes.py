import numpy as np 
import pandas as pd 
import requests, json
import tokens
token = tokens.noaa



def read_csv(f="atlantic.csv"):
	return pd.read_csv(f)

def get_rainfall_json(station, startdate, enddate):
	url = "https://www.ncdc.noaa.gov/cdo-web/api/v2/data?datasetid=PRECIP_15&stationid=" + station 
	url += "&units=metric&startdate=" + startdate + "&enddate=" + enddate
	headers = {'token': token}
	r = requests.get(url, headers=headers)
	json_obj = json.loads(r.text)
	return json_obj

def get_rainfall_data(station, startdate, enddate):
	data = get_rainfall_json(station, startdate, enddate)
	results = data['results']
	return [(item['date'], item['value']) for item in results]

def get_stations(latitude, longitude):
	tuples = [
		str(latitude - 0.05), 
		str(longitude - 0.05), 
		str(latitude + 0.05), 
		str(longitude + 0.05)
	]
	extent = ",".join(tuples)
	url = "https://www.ncdc.noaa.gov/cdo-web/api/v2/stations?extent=" + extent
	headers = {'token': token}
	r = requests.get(url, headers=headers)
	json_obj = json.loads(r.text)
	return [item['id'] for item in json_obj['results']]


# print get_rainfall_data("010008", "2010-05-01", "2010-05-31")
url2 = "https://www.ncdc.noaa.gov/cdo-web/api/v2/stations?extent=47.5204,-122.2047,47.6139,-122.1065"
stations = get_stations(47.5204,-122.2047)
for i in range(len(stations)):	
	print get_rainfall_json(stations[i], "2008-06-01", "2009-03-03")