import requests

# post data to url and save the information into a file
my_data = {"name": "Adro", "email": "abc@abc.com"}
r = requests.post("https://www.w3schools.com/php/welcome.php", data=my_data)

f = open("./post.html", "w+")
f.write(r.text)