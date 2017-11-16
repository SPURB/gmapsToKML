import Vue from 'vue';
import App from './App.vue';
import * as VueGoogleMaps from 'vue2-google-maps'

import normalize from './assets/css/vendor/normalize.css';
import skeleton from './assets/css/vendor/skeleton.2.0.4.css';
import sass from './assets/css/style.sass';

new Vue({
  el: '#app',
  render: h => h(App)
})

// GET from
//https://maps.googleapis.com/maps/api/js?key=AIzaSyBdXi54F8bicR3FKfCDBQixW-9ZGFfR6pc