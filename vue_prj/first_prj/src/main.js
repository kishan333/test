import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import VueResource from 'vue-resource'

Vue.use(VueResource)
Vue.config.productionTip = false

Vue.http.options.root = '/root'
Vue.http.headers.common['Authorization'] = 'Basic YXBpOnBhc3N3b3Jk'
Vue.http.headers.common['Access-Control-Allow-Origin'] = '*'

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
