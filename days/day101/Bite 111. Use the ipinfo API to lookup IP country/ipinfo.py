import json

import requests

IPINFO_URL = 'http://ipinfo.io/{ip}/json'


def get_ip_country(ip_address):
    """Receives ip address string, use IPINFO_URL to get geo data,
       parse the json response returning the country code of the IP"""
    with requests.Session() as s:
        resp = s.get(IPINFO_URL.format(ip=ip_address))
    resp.raise_for_status()
    return resp.json()['country']


if __name__ == "__main__":
    print(get_ip_country('187.190.38.36'))     # MX
    #print(get_ip_country('185.161.200.10'))    # JP
