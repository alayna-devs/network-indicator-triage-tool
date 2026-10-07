import requests
import csv
from operator import itemgetter


# 1. open the file
with open("ip_data.txt", "r", encoding="utf-8") as txt_file, \
    open("output.csv", "w", newline="", encoding="utf-8") as csv_file:
        
    writer = csv.writer(csv_file)
    writer.writerow(["IP Address", "API Status", "Country", "City", "Zip Code", "ISP", "Organization"])
    
    #2. loop line by line directly through the file object
    for line in txt_file:
        #3. clean up whitespace and hidden \n characters
        target_ip = line.strip()
        
        #4. skip blank lines if there are any in your file
        if not target_ip:
            continue
        
        try:
            #5. use the cleaned ip variable in your URL
            url = f"http://ip-api.com/json/{target_ip}"
            # response object often called r
            response = requests.get(url)
            # converts json "web data" into python "clean data"
            data = response.json()

            # unpacking data
            status, country, city, zip_code, isp, org = itemgetter("status", "country", "city", "zip", "isp", "org")(data)
            
            print(f"\n--- Triage Report for {target_ip} ---")
            print("Status Code: ", response.status_code)
            print("API Status: ", status)
            print(f"{target_ip} organization is {org} and it's country is located in {country}, city of {city}, and zip code {zip_code}, with an ISP of {isp}.")
            
            writer.writerow([target_ip, status, country, city, zip_code, isp, org])
            writer.writerow([])
            
        except KeyError as e:
            # if the API fails from dict key error, print what the API actually said to help debug
            print(f"\n Failed to parse {target_ip}. API Response: {data}")
            