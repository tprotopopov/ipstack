#!/usr/bin/env python3

import sys
import requests
import json


def get_location(ip, access_key):
    """
    Query the IPStack API for the geolocation of an IP address.
    """
    url = f"http://api.ipstack.com/{ip}?access_key={access_key}"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for request failures
    except requests.RequestException as e:
        print(f"Error in connection: {e}", file=sys.stderr)
        sys.exit(1)

    data = response.json()
    if "latitude" in data and "longitude" in data:
        return data["latitude"], data["longitude"]
    else:
        print("Could not retrieve location data.", file=sys.stderr)
        sys.exit(1)


def main():
    if len(sys.argv) != 3:
        print("Usage: ip_query.py [IP address] [API access key]", file=sys.stderr)
        sys.exit(1)

    ip = sys.argv[1]
    access_key = sys.argv[2]

    latitude, longitude = get_location(ip, access_key)

    # Print results in a manner that they can be easily piped into another command-line tool
    print(json.dumps({"latitude": latitude, "longitude": longitude}))


if __name__ == "__main__":
    main()
