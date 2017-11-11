# import the requests package   : pip3 install requests
import requests

# Specify the url
r = requests.get("http://google.com")
# print the status code
print("Status:", r.status_code)

# create file in memory
f = open("./page.html", "w+")
# write to file the text content to the webpage
f.write(r.text)