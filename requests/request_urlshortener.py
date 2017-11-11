import requests
import simplejson as json


# This will return a 'Daily limit exceeded' error, needs an API key
# sets the url for the request
url = 'https://www.googleapis.com/urlshortener/v1/url'
# sets the url that needs to be shortned as json
payload = {"longUrl": "https://github.com/HurricaneInteractive"}
# defines header
headers = {"Content-Type": "application/json"}
# makes the request and pass in url, payload and header
r = requests.post(url, json=payload, headers=headers)

# prints error code
print(json.loads(r.text)["error"]["code"])
# prints headers returned from the server
print(r.headers)