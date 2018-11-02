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
      path: '/word',
      name: 'word-main',
      component: require('@/pages/WordPage/WordMainPage').default
    },
    {
      path: '*',
      redirect: '/'
    }
  ]
})
