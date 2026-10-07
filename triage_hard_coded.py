import requests
from operator import itemgetter

target_ip = "1.1.1.1" #CloudFlare
url = f"http://ip-api.com/json/{target_ip}"

# we have a Response object called r
response = requests.get(url)

# converts json "web data" into python "clean data"
data = response.json()

# Unpacking your data using itemgetter
status, country, city, zip, isp, org = itemgetter("status", "country", "city", "zip", "isp", "org")(data)

print("Status Code: ", response.status_code)
print("Dictionary Keys: ", data.keys())
print("API Status: ", status)
#readable
print(f"{target_ip} organization is {org} and it's country is located in {country}, city of {city}, and zip code {zip}, with an ISP of {isp}.")