<template>
  <div id="container">
    <app-header></app-header>
    <app-formmap></app-formmap>
  </div>
</template>

<script>
import Header from './components/Header.vue';
import FormMap from './components/FormMap.vue'

export default {
  components: {
    'app-header': Header,
    'app-formmap': FormMap
  } 
}
</script>

<style lang="scss">
</style>
