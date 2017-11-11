# import requests library
import requests

# create some url parameters
params = {"q" : "pizza"}
# set url path and pass in parameters
r = requests.get("http://www.bing.com/search", params=params)
print("Status", r.status_code)

# create and write to file with returned text content
f = open("./pizza.html", "w+")
f.write(r.text)