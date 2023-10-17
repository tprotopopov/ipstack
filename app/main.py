#!/usr/bin/env python3

import sys
import requests
import json


def get_location(ip, access_key):
    """
    Query the IPStack API for the geolocation of an IP address.
    """
    url = f"http://api.ipstack.com/{ip}?access_key={access_key}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        latitude = data.get("latitude")
        longitude = data.get("longitude")

        if latitude is not None and longitude is not None:
            return latitude, longitude
        else:
            print("Could not retrieve location data. Data might be missing.", file=sys.stderr)
            sys.exit(1)
    else:
        print(f"Error: Received status code {response.status_code} from the server", file=sys.stderr)
        sys.exit(1)


def main():
    if len(sys.argv) != 3:
        print("Usage: ip_query.py [IP address] [API access key]", file=sys.stderr)
        sys.exit(1)

    ip = sys.argv[1]
    access_key = sys.argv[2]
    latitude, longitude = get_location(ip, access_key)
    print(json.dumps({"latitude": latitude, "longitude": longitude}))


if __name__ == "__main__":
    main()
