#!/usr/bin/env python3

import sys
import requests
import json
import argparse
import os


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
    parser = argparse.ArgumentParser(
        description="""
        Query the IPStack API for the geolocation of an IP address.
        This script requires two inputs:
        1. An IP address passed directly as a command-line argument.
        2. The IPStack access key stored in a file named 'token' within the application directory.

        Example usage:
        python script.py YOUR_IP_ADDRESS

        Replace 'YOUR_IP_ADDRESS' with the actual IP address you wish to query.
        The script will automatically read the access key from the 'token' file.
        """,
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument('ip', help="The IP address to query")
    args = parser.parse_args()
    ip = args.ip

    script_dir = os.path.dirname(os.path.abspath(__file__))
    token_file_path = os.path.join(script_dir, 'token')
    try:
        with open(token_file_path, 'r') as file:
            access_key = file.read().strip()
    except FileNotFoundError:
        print("Error: 'token' file not found. Please ensure the 'token' file exists in the application directory.",
              file=sys.stderr)
        sys.exit(1)

    if not access_key:
        print("Error: The 'token' file is empty. Please store the IPStack access key in the 'token' file.",
              file=sys.stderr)
        sys.exit(1)

    latitude, longitude = get_location(ip, access_key)
    print(json.dumps({"latitude": latitude, "longitude": longitude}))


if __name__ == "__main__":
    main()
