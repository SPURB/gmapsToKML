import urllib.request
import json

request_url = 'https://maps.googleapis.com/maps/api/place/radarsearch/json?location=-23.5453653,-46.6357204&radius=125&type=parking&key=AIzaSyBdXi54F8bicR3FKfCDBQixW-9ZGFfR6pc'

with urllib.request.urlopen(request_url) as url:
    response = url.read()

charset = url.info(). get_content_charset('utf-8')  # UTF-8 is the JSON default
data = json.loads(response.decode(charset))

print(json.dumps(data['results'], indent=4))