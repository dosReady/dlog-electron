<template>
  <div id="app" class="container">
    <div class="row">
      <!-- <top-menu></top-menu> -->
      <div id="side-menu-div" class="col">
        <side-menu></side-menu>
      </div>
      <div id="content" class="col">
        <router-view></router-view>
      </div>
    </div>
  </div>
</template>

<script>
// import TopMenu from '@/components/CommonPage/TopMenu'
import SideMenu from '@/components/CommonPage/SideMenu'
export default {
  name: 'dlog',
  components: {
    SideMenu
    // TopMenu
  }
}
</script>

<style>
::-webkit-scrollbar {
  display: none;
}
div.container {
  margin: 0;
  padding: 0;
}
div.content {
  margin: 0;
  padding: 0;
  width: 100%!important;
  background: rgba(249,247,232,1)
}
div.side-menu-div {
  margin: 0;
  padding: 0;
  width: 100%!important;
}
</style>
