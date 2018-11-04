import Vue from 'vue'
import axios from 'axios'
import App from './App'
import router from './router'
import store from './store'
import {PythonShell} from 'python-shell'
import ChildProcess from 'child_process'
import util from 'util'
import path from 'path'

import 'bootstrap'
import 'bootstrap/dist/css/bootstrap.min.css'

if (!process.env.IS_WEB) Vue.use(require('vue-electron'))
Vue.http = Vue.prototype.$http = axios
Vue.config.productionTip = false

// My Code
let curdirname = path.join(__dirname, '../../../../')
if (process.env.NODE_ENV !== 'production') {
  curdirname = path.join(process.cwd(), './src/')
}
console.log('Electron Path: ' + curdirname)

const execFile = util.promisify(ChildProcess.execFile)
Vue.prototype.$PythonShell = PythonShell
Vue.prototype.$ChildProcess = ChildProcess
Vue.prototype.$curdirname = curdirname

Vue.pyrouterFn = Vue.prototype.$pyrouterFn = async function (pyfile, args) {
  let pathval = path.join(__dirname, './python')
  if (process.env.NODE_ENV !== 'production') {
    pathval = path.join(process.cwd(), './src/python')
  }
  if (process.env.NODE_ENV === 'production') {
    const {stdout, stderr} = await execFile(`${pathval}\\${pyfile}.exe`, ['production', args])
    if (stderr) throw stderr
    let obj = JSON.parse(stdout)
    obj.argv.splice(0, 1)
    return obj
  } else {
    // const {stdout, stderr} = await execFile('python', [`${pathval}\\${pyfile}.py`, 'development', args])
    const {stdout, stderr} = await execFile(`${pathval}\\${pyfile}.exe`, ['development', args])
    if (stderr) throw stderr
    let obj = JSON.parse(stdout)
    obj.argv.splice(0, 1)
    return obj
  }
}
// End My Code

/* eslint-disable no-new */
new Vue({
  components: { App },
  router,
  store,
  template: '<App/>'
}).$mount('#app')
