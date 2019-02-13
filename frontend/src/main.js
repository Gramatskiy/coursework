import '@babel/polyfill'
import './plugins/vuetify'
import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import { mapActions, mapGetters } from 'vuex'

import VueLodash from 'vue-lodash'
import Fragment from 'vue-fragment'

import VueClickOutside from 'vue-click-outside'

import * as VueGoogleMaps from 'vue2-google-maps'
import translations from './translations.json'

import VueTranslate from 'vue-translate-plugin'

Vue.use(VueTranslate)
Vue.locales(translations)

Vue.config.productionTip = false

Vue.use(Fragment.Plugin)
Vue.use(VueLodash)
Vue.use(VueGoogleMaps, {
  load: {
    key: 'ENTER_YOUR_MAP_API_KEY',
    libraries: 'places'
  }
})

Vue.use(require('vue-moment'))
Vue.mixin({
  methods: {
    ...mapGetters([
      'getUser'
    ]),
    ...mapActions([
      'setActiveMenuItemName',
      'setJSONWebToken',
      'setUser',
      'setIsAdmin',
      'setIsProvider',
      'setIsPremium',

      'removeJSONWebToken',
      'removeUser',
      'removeIsAdmin',
      'removeIsProvider',
      'removeIsPremium'
    ])
  }
})

Vue.directive('click-outside', VueClickOutside)
new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
