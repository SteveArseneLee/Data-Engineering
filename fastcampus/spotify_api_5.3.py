import sys
import requests
import base64
import json
import logging

client_id  = "97fe3570d286403297627bee98da65ed"
client_secret = "f18af107dea4467fa06ca91f42672a16"

def main():
    headers = get_headers(client_id,client_secret)
    # print(headers)
    # sys.exit(0)
    
    params = {
        "q" : "BTS",
        "type" : "artist",
        "limit":"5"
    }
    
    r = requests.get("https://api.spotify.com/v1/search", params=params, headers=headers)
    print(r.text)
    print(r.status_code)
    
    
def get_headers(client_id, client_secret):
    endpoint = "https://accounts.spotify.com/api/token"
    encoded = base64.b64encode("{}:{}".format(client_id, client_secret).encode('utf-8')).decode('ascii')

    headers = {
        "Authorization": "Basic {}".format(encoded)
    }
    payload = {
        "grant_type": "client_credentials"
    }

    r = requests.post(endpoint, data=payload, headers=headers)

    # print(r.status_code)
    # print(r.text)
    # print(type(r.text))
    # sys.exit(0)

    # access_token = json.loads(r.text)
    # print(type(access_token))
    # sys.exit(0)
    access_token = json.loads(r.text)['access_token']
    headers = {
        "Authorization" : "Bearer {}".format(access_token)
    }
    return headers

if __name__=='__main__':
    main()
