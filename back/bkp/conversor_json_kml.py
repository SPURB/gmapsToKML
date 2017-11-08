import json
from pprint import pprint
import simplekml

search_def = "rangel_pestana"
search_def_in = search_def+".json"
search_def_out = search_def+ ".kml"

kml = simplekml.Kml()

with open(str(search_def_in)) as data_file:
    data = json.load(data_file)["results"]

for geometry in data:
    # place_id = geometry["place_id"]
    lng = geometry["geometry"]["location"]["lng"]
    lat = geometry["geometry"]["location"]["lat"]

    # print(place_id, lat, lng)
    kml.newpoint(name = "I", coords = [(lng,lat)])

kml.save(str(search_def_out))


#https://maps.googleapis.com/maps/api/place/radarsearch/json?location=-23.5502797,-46.63177&radius=500&type=parking&key=AIzaSyBdXi54F8bicR3FKfCDBQixW-9ZGFfR6pc
# A
# rua_vitoria_av_rio_branco_500m
# -23.5388463,-46.6406349

# B
# rua_washington_luis_av_prestes_maia_500m
# -23.5378713,-46.6337276

# C
# av_estado_av_mercurio
# -23.541376,-46.6285956

# D
# praca_ramos_rua_24_maio 
# -23.544949,-46.6389006

# E
# viaduto_jacarei_rua_santo_amaro
# -23.5514676,-46.6402743

# F
# praca_ragueb
# -23.5448529,-46.6320306

# G
# rua_do_carmo
# -23.550984,-46.6316644

# H 
# parque_dom_pedro
# -23.5452112,-46.6276579

# I 
# rangel_pestana
# -23.5502797,-46.63177