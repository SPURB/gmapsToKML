import simplekml
import json
import urllib.request
from pprint import pprint

request_url = 'https://maps.googleapis.com/maps/api/place/radarsearch/json?location=-23.5453653,-46.6357204&radius=125&type=parking&key=SUA-CHAVE-DA-API-DE-GMAPS'
# location: two numbers
# radius: a number 
# type: an item from list
# key: google api key

with urllib.request.urlopen(request_url) as url:
    response = url.read()

charset = url.info(). get_content_charset('utf-8')
data = json.loads(response.decode(charset))

# print(json.dumps(data, indent=4))

search_name = "nome_arquivo"
search_name_out = search_name+ ".kml"
kml = simplekml.Kml()

for geometry in data['results']:
    # place_id = geometry["place_id"]
    lng = geometry["geometry"]["location"]["lng"]
    lat = geometry["geometry"]["location"]["lat"]

    # print(place_id, lat, lng)
    kml.newpoint(name = search_name, coords = [(lng,lat)])

kml.save(str(search_name_out))
print(search_name_out, 'created')