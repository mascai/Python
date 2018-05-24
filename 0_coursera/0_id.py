import requests

def get_location_info():
	return requests.get("http://freegeoip.net/json/").json()

if __name__ == "__main__":
	data = get_location_info()
	for key, item in data.items():
		print (key, "---", item)


'''
metro_code --- 0
region_name --- Moscow
time_zone --- Europe/Moscow
city --- Moscow
zip_code --- 102630
country_code --- RU
country_name --- Russia
longitude --- 37.2156
latitude --- 55.052
region_code --- MOW

'''