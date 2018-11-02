import Vue from 'vue'
import axios from 'axios'
import App from './App'
import router from './router'
import store from './store'
import {PythonShell} from 'python-shell'

import 'bootstrap'
import 'bootstrap/dist/css/bootstrap.min.css'

if (!process.env.IS_WEB) Vue.use(require('vue-electron'))
Vue.http = Vue.prototype.$http = axios
Vue.config.productionTip = false
Vue.PythonShell = Vue.prototype.$PythonShell = PythonShell
/* eslint-disable no-new */
new Vue({
  components: { App },
  router,
  store,
  template: '<App/>'
}).$mount('#app')
