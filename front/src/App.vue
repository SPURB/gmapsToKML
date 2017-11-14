<template>
  <div id="container">
    <app-header></app-header>
    <app-formmap></app-formmap>
  </div>
</template>

<script>
import * as VueGoogleMaps from 'vue2-google-maps';
import Vue from 'vue';
import Header from './components/Header.vue';
import FormMap from './components/FormMap.vue';


Vue.use(VueGoogleMaps, {
  load: {
    key: 'AIzaSyBdXi54F8bicR3FKfCDBQixW-9ZGFfR6pc',
    // v: 'OPTIONAL VERSION NUMBER',
    libraries: 'places' //// If you need to use place input
  }
});

export default {
  components: {
    'app-header': Header,
    'app-formmap': FormMap
  }
}
</script>
