<template>
  <div id="app">
    <top-menu></top-menu>
    <router-view></router-view>
  </div>
</template>

<script>
import TopMenu from '@/components/CommonPage/TopMenu'
export default {
  name: 'dlog',
  components: {TopMenu}
}
</script>

<style>
::-webkit-scrollbar { 
  display: none; 
}
</style>
