import requests
import json


# === request for token that need before GET ===
def _request_token(client_id, client_secret):
    """
    function that request new access token from Spotify server
    """
    headers = {'Accept':'application/json'}
    data = [('grant_type','client_credentials')]
    token = requests.post("https://accounts.spotify.com/api/token", \
                              params=None, headers=headers, data=data, \
                              auth=(client_id, client_secret))
    return token


# === creation json file of request by track or artist name ===
def get_json_file(json_file, name, type, client_id, client_secret):
    """
    make request to Spotify server by track name and write json file
    """
    access_token = _request_token(client_id, client_secret)
    headers = {'Authorization':'Bearer ' + access_token.json()['access_token'],}
    params =(('q', name), ('type', type))
    res = requests.get("https://api.spotify.com/v1/search", \
                       headers=headers, params=params)
    with open(json_file, 'w') as f:
        json.dump(res.json(), f, indent=2)
    return None
