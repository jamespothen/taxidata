import json
import requests
import config

outfile = open("taxi2011.csv", "w")

endpoint = "https://data.cityofnewyork.us/resource/uwyp-dntv.json"
# parameters = {'$limit':20, '$$app_token':'config.app_token'}
parameters = {"$limit": 200000000, "$$app_token": "config.app_token"}

requestobj = requests.get(endpoint, params=parameters)
ridelist = json.loads(requestobj.text)

headers = ridelist[0].keys()

print(
    "vendorid, tpep_pickup_datetime, dropoff_datetime, passenger_count, trip_distance, pickup_longitude, pickup_latitude, ratecodeid, store_and_fwd_flag, dropoff_longitude, dropoff_latitude, payment_type, fare_amount, extra, mta_tax, tip_amount, tolls_amount, total_amount",
    file=outfile,
)

for ride in ridelist:
    for header in headers:
        if (
            header == "store_and_fwd_flag"
            or header == "pickup_location"
            or header == "dropoff_location"
        ):
            continue
        print(f"{ride[header]}, ", end="")
        print(f"{ride[header]}, ", end="", file=outfile)
    print("")
    print("")
    print("", file=outfile)

outfile.close()
