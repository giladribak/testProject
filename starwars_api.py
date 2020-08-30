import swapi
import json
import urllib.request

swapi.settings.BASE_URL = "https://swapi.dev/api"

#for planet in swapi.get_all("planets").order_by("diameter"):
#    print(planet.name , planet.diameter)
url = 'https://swapi.dev/api/films'
with urllib.request.urlopen(url) as file:
    source = file.read()
data = json.loads(source)
for item in data['results']:
    print(item['title'] , item['url'])

url2 = 'https://swapi.dev/api/planets/?page=3'
with urllib.request.urlopen(url2) as file2:
    source2 = file2.read()
data2 = json.loads(source2)
for item in data2['results']:
    print(item)

url3 = 'https://swapi.dev/api'
with urllib.request.urlopen(url3) as file3:
    source3 = file3.read()
data3 = json.loads(source3)
for item in data3:
    print(item)
