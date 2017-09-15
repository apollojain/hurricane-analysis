import urllib, wikipedia, re
from bs4 import BeautifulSoup


def get_soup_item(url):
	r = urllib.urlopen(url).read()
	soup = BeautifulSoup(r, "lxml")
	return soup

def process_wind(wind):
	return wind.string.split(' ')[0]

def get_wind(soup):
	pattern = re.compile(r'Highest winds')
	tr = soup.find('th', text=pattern).parent
	span = tr.findChildren('span')[0]
	# wind = ''.join(td.findAll(text=True))
	# return process_pressure(pressure)
	return process_wind(span)

def process_pressure(pressure):
	return pressure.split(" ")[0]

def get_pressure(soup):
	pattern = re.compile(r'Lowest pressure')
	tr = soup.find('th', text=pattern).parent
	td = tr.findChildren('td')[0]
	pressure = ''.join(td.findAll(text=True))
	return process_pressure(pressure)

def process_damage(cost): 
	# FILL IN HERE
	return cost.split('\n')[0]

def get_damage(soup):
	pattern = re.compile(r'Damage')
	tr = soup.find('th', text=pattern).parent
	td = tr.findChildren('td')[0]
	cost = ''.join(td.findAll(text=True))
	return process_damage(cost)

def process_fatalities(fatalities):
	# FILL IN HERE
	return fatalities

def get_fatalities(soup):
	# def get_range
	pattern = re.compile(r'Fatalities')
	tr = soup.find('th', text=pattern).parent
	td = tr.findChildren('td')[0]
	fatalities = td.string
	# fatalities = int(f_str.split(' ')[0].split('-')[0])
	return process_fatalities(fatalities)


def get_affected_areas(soup):
	pattern = re.compile(r'Areas affected')
	tr = soup.find('th', text=pattern).parent
	cell = tr.findChildren('td')[0]
	countries = cell.findChildren('a')
	return [c.string for c in countries]

def get_hurricane_info(hurricane, year): 
	wiki = wikipedia.page("Hurricane " + hurricane + " " + year)
	url = wiki.url 
	soup = get_soup_item(url)
	results = {}
	results["Fatalities"] = get_fatalities(soup)
	results["Damage"] = get_damage(soup)
	results["Affected Areas"] = get_affected_areas(soup)
	return results

soup = get_soup_item('https://en.wikipedia.org/wiki/Hurricane_Katrina')
print get_wind(soup)
