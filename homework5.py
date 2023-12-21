import requests
import csv
import time

iss_api_url = "http://api.open-notify.org/iss-now.json"

csv_filename = "iss_location_data.csv"

with open(csv_filename, mode='w', newline='') as csv_file:
    fieldnames = ['timestamp', 'latitude', 'longitude']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    print(1111111111111222222222)
    while True:
        response = requests.get(iss_api_url)
        data = response.json()
        timestamp = time.time()
        latitude = data['iss_position']['latitude']
        longitude = data['iss_position']['longitude']
        writer.writerow({'timestamp': timestamp, 'latitude': latitude, 'longitude': longitude})
        time.sleep(5)

        print(2222222222222222222222)

