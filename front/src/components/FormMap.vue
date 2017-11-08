<template>
    <div class='row'>
        <form id="kml_data" onsubmit="retrieveData()">
            <div class="row">
                <div class="ten columns">
                  <label for="location">Localização da pesquisa</label>
                  <input 
                    class="u-full-width" 
                    id="address" 
                    type="text" 
                    placeholder="Exemplo: Rua Libero Badaró, 405, Centro,  São Paulo">
                </div>

                <div class="two columns">
                  <label for="submitPoint">Ponto</label>
                  <input 
                    id="submitPoint" 
                    type="button" 
                    value="Localizar" 
                    class="button-primary">
                </div>
            </div>

            <div class="row">
                <div class="three columns submit_forms">
                    <label for='rangeInput'>Raio de pesquisa</label>
                    <!-- <input type="range" name="rangeInput" min="0" max="500" onchange="updateTextInput(this.value);"> -->
                    <input 
                        type="range" 
                        name="rangeInput" 
                        min="0" 
                        max="1000" 
                        v-model.number="formData.radiusInput">
               </div>
                <div class="three columns submit_forms">
                    <label for='radiusInput'>Raio (metros)</label>
                    <input 
                        type="number" 
                        id="radiusInput" 
                        value="500" 
                        v-model.number="formData.radiusInput">
                </div>
                <div class="four columns">
                  <label for="api_types">Locais</label>
                  <select class="u-full-width" 
                    id="api_types"
                    v-model="formData.locationType">
                    <option 
                        v-for="option in places" 
                        v-bind:value="option">
                        {{ option.text }}
                    </option>
                  </select>
                  <p class="fonte_citacoes">Fonte: <a href="https://developers.google.com/places/supported_types" target="blank">Tipos de locais</a> | API Google Maps</p>
                </div>
                <div class="two columns">
                    <label for='refreshPoints'>Raio e locais</label>
                    <button class="button-primary" 
                        type="submit" 
                        id="refreshPoints">Atualizar</button>
                </div>
            </div>
        </form>
        <div class="row" id="map"></div>
        <div class="row">
            <button 
                class="button-primary" 
                type="submit" 
                onclick="submitDataToServer()" 
                id="kmlMaker">Gerar arquivo KML de {{ formData.locationType.text  }}</button>
        </div>
    </div>
</template>
<script>
export default{
    data: function(){
        return{
            title:"Conversão de locais definidos na API do google maps em KML",
            mapSearchRadius: 1000,
            mapViewLatitude: -23.5453653,
            mapViewLongitude: -46.6357204,
            mapViewZoom: 15,
            formData: {
              radiusInput: 500,
              locationType:'',
            },
            places: [
                {value: "default", text: "Selecione um tipo de local"},
                {value: "accounting", text: "contabilidade"},
                {value: "airport", text: "aeroporto"},
                {value: "amusement_park", text: "parque de diversões"},
                {value: "aquarium", text: "aquário"},
                {value: "art_gallery", text: "galeria de arte"},
                {value: "atm", text: "atm"},
                {value: "bakery", text: "padaria"},
                {value: "bank", text: "banco"},
                {value: "bar", text: "bar"},
                {value: "beauty_salon", text: "salão de beleza"},
                {value: "bicycle_store", text: "loja de bicicletas"},
                {value: "book_store", text: "livraria"},
                {value: "bowling_alley", text: "boliche"},
                {value: "bus_station", text: "estação de onibus"},
                {value: "cafe", text: "café"},
                {value: "campground", text: "área de camping"},
                {value: "car_dealer", text: "concessionária"},
                {value: "car_rental", text: "aluguel de carros"},
                {value: "car_repair", text: "mecânica"},
                {value: "car_wash", text: "lava-jato"},
                {value: "casino", text: "casino"},
                {value: "cemetery", text: "cemitério"},
                {value: "church", text: "igreja"},
                {value: "city_hall", text: "prefeitura"},
                {value: "clothing_store", text: "loja de roupas"},
                {value: "convenience_store", text: "loja de conveniência"},
                {value: "courthouse", text: "tribunal"},
                {value: "dentist", text: "dentista"},
                {value: "department_store", text: "loja de departamento"},
                {value: "doctor", text: "médico"},
                {value: "electrician", text: "eletricista"},
                {value: "electronics_store", text: "loja de eletrônicos"},
                {value: "embassy", text: "embaixada"},
                {value: "fire_station", text: "corpo de bombeiros"},
                {value: "florist", text: "florista"},
                {value: "funeral_home", text: "funerária"},
                {value: "furniture_store", text: "loja de móveis"},
                {value: "gas_station", text: "posto de gasolina"},
                {value: "gym", text: "academia"},
                {value: "hair_care", text: "cabeleleiro"},
                {value: "hardware_store", text: "loja de ferragens"},
                {value: "hindu_temple", text: "templo hindu"},
                {value: "home_goods_store", text: "loja de bens domésticos"},
                {value: "hospital", text: "hospital"},
                {value: "insurance_agency", text: "agência de seguros"},
                {value: "jewelry_store", text: "joalheria"},
                {value: "laundry", text: "lavanderia"},
                {value: "lawyer", text: "advogado"},
                {value: "library", text: "biblioteca"},
                {value: "liquor_store", text: "casa de bebidas"},
                {value: "local_government_office", text: "escritório de governo local"},
                {value: "locksmith", text: "chaveiro"},
                {value: "lodging", text: "alojamento"},
                {value: "meal_delivery", text: "restaurante delivery"},
                {value: "meal_takeaway", text: "refeições para viagem"},
                {value: "mosque", text: "mesquita"},
                {value: "movie_rental", text: "locadora"},
                {value: "movie_theater", text: "cinema"},
                {value: "moving_company", text: "carreto"},
                {value: "museum", text: "museu"},
                {value: "night_club", text: "clube noturno"},
                {value: "painter", text: "pintor"},
                {value: "park", text: "parque"},
                {value: "parking", text: "estacionamento"},
                {value: "pet_store", text: "loja de animais"},
                {value: "pharmacy", text: "farmacia"},
                {value: "physiotherapist", text: "fisioterapeuta"},
                {value: "plumber", text: "encanador"},
                {value: "police", text: "polícia"},
                {value: "post_office", text: "agência dos correios"},
                {value: "real_estate_agency", text: "agência imobiliária"},
                {value: "restaurant", text: "restaurante"},
                {value: "roofing_contractor", text: "concerto de telhados"},
                {value: "rv_park", text: "estacionamento de trailers"},
                {value: "school", text: "escola"},
                {value: "shoe_store", text: "loja de sapatos"},
                {value: "shopping_mall", text: "centro de compras"},
                {value: "spa", text: "spa"},
                {value: "stadium", text: "estádio"},
                {value: "storage", text: "armazenamento"},
                {value: "store", text: "loja"},
                {value: "subway_station", text: "estação de metrô"},
                {value: "synagogue", text: "sinagoga"},
                {value: "taxi_stand", text: "ponto de taxi"},
                {value: "train_station", text: "estação de trem"},
                {value: "transit_station", text: "estação de trânsito"},
                {value: "travel_agency", text: "agência de viagens"},
                {value: "university", text: "universidade"},
                {value: "veterinary_care", text: "cuidado veterinário"},
                {value: "zoo", text:"jardim zoológico"}
            ]
        }
    }, 
    methods:{
      initMap: function(){
        map = new google.maps.Map(document.getElementById('map'), {
          center: {lat:this.mapViewLatitude, lng:this.mapViewLongitude},
          zoom: this.mapViewZoom
        });
        infowindow = new google.maps.InfoWindow();
        var service = new google.maps.places.PlacesService(map);
        service.nearbySearch({
          location: {lat:this.mapViewLatitude, lng:this.mapViewLongitude},
          radius: this.mapSearchRadius,
          type: ['university']
        }, this.callback);
        var searchR = new google.maps.Circle({
            strokeColor: '#FF0000',
            strokeOpacity: 0.8,
            strokeWeight: 1,
            fillOpacity: 0,
            map: map,
            center: {lat:this.mapViewLatitude, lng:this.mapViewLongitude},
            radius: this.mapSearchRadius
        }); this.submitPoint();
      },
      submitPoint: function(){
          document.getElementById('submitPoint').addEventListener('click', function() {
          var address = document.getElementById('address').value;
          new google.maps.Geocoder().geocode({'address': address}, function(results, status) {
            if (status === 'OK') {
              map.setCenter(results[0].geometry.location);
              var marker = new google.maps.Marker({
                map: map,
                position: results[0].geometry.location
              })
              console.log(marker.position.lat(this));
              console.log(marker.position.lng(this));
            } 
            else {
              alert('Falha na geocodificação: Insira um endereço válido');
              console.log(status);
            }
          });
        });
        },
      callback: function(results, status){
        if (status === google.maps.places.PlacesServiceStatus.OK) {
          for (var i = 0; i < results.length; i++) {
              this.createMarker(results[i]);
          }
        }
      },
      createMarker: function(place){
        var marker = new google.maps.Marker({
            map: map,
            position: place.geometry.location
        });
        google.maps.event.addListener(marker, 'click', function() {
            infowindow.setContent(place.name);
            infowindow.open(map, this);
        });
      }
    }
}
</script>
