import Vue from 'vue'
import App from './App.vue'

import normalize from './assets/css/vendor/normalize.css';
import skeleton from './assets/css/vendor/skeleton.2.0.4.css';
import sass from './assets/css/style.sass';


vm = new Vue({
  el: '#app',
  render: h => h(App)
})

