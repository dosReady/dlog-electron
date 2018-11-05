import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'landing-page',
      component: require('@/pages/LandingPage').default
    },
    {
      path: '/nwmonitor',
      name: 'newmonitor-main',
      component: require('@/pages/ContentsPage/NwMonitorPage').default
    },
    {
      path: '/options',
      name: 'option-main',
      component: require('@/pages/CommonPage/OptionPage').default
    },
    {
      path: '*',
      redirect: '/'
    }
  ]
})
