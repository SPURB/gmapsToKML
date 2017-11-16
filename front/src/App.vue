<template>
  <div id="container">
    <div class="row">
        <div class="ten columns">
          <label>Localização da pesquisa</label>
          <input 
            v-model="address"
            class="u-full-width" 
            type="text" 
            >
        </div>
        <div class="two columns submit_forms">
          <label><br></label>
          <input 
            name="btnLocate"
            @click="changeCenter"
            type="button" 
            value="Localizar" 
            class="button-primary">
        </div>
    </div>

    <div class="row" id="requestInfo">
      <table class="u-full-width">
        <thead>
            <tr><td>string to geocode:</td><td> {{ address }}</td></tr>
            <tr><td>lat: </td><td>{{ changingCenter.lat }}</td></tr>
            <tr><td>lng: </td><td>{{ changingCenter.lng }}</td></tr>
        </thead>
      </table>
    </div>
    <gmap-map 
        :center="changingCenter"
        @center_changed="updateCenterfromView"
        :zoom="zoom">
    </gmap-map>
  </div>
</template>

<script>
import * as VueGoogleMaps from 'vue2-google-maps';
import Vue from 'vue';


Vue.use(VueGoogleMaps, {
  load: {
    key: 'AIzaSyBdXi54F8bicR3FKfCDBQixW-9ZGFfR6pc'
  }
});

export default {
    data: function(){
        return {
            displayMap: true,
            address:'Praça da Sé, São Paulo',
            changingCenter: {
                lat: -23.5453653, 
                lng: -46.6357204
            },
            zoom: 15,
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
    methods: {
        changeCenter: function(lat, lng){
            this.displayMap = true;
            this.changingCenter = {
              lat: 1.38 + Math.random() * 0.3,
              lng: 103.8 + Math.random() * 0.1
            };
          this.geocode(this.address);
        }, 
        geocode: function(strAddress){
          if (this.displayMap) {
            strAddress = this.address;
            var map = new google.maps.Map(document.getElementsByClassName('vue-map')[0], {zoom: this.zoom, center: this.changingCenter});
            var geocoder = new google.maps.Geocoder();
            // console.log(geocoder)
            geocoder.geocode({'address': strAddress}, function(results, status){
              if (status === 'OK'){
                var formatted_address = results[0].formatted_address;
                var newLat = results[0].geometry.location.lat();
                var newLng = results[0].geometry.location.lng();
                console.log(formatted_address+' / '+ newLat + ' / '+ newLng);
                console.log(this)
              }
              else {
                alert('geoceder failed tipa novamente')
              }
            })
          }
        }, 
        updateCenterfromView: function(newCenter){
            this.newCenter = {
              lat: newCenter.lat(),
              lng: newCenter.lng(),
            }
        }
    }
}
</script>
