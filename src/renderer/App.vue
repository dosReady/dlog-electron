<template>
  <div id="app" class="row">
      <div id="side-menu-div" class="col-3 bg-blue-grey-700">
        <side-menu></side-menu>
      </div>
      <div id="content" class="col-9 px-0">
        <router-view></router-view>
      </div>
  </div>
</template>

<script>
import SideMenu from '@/pages/CommonPage/SideMenu'
export default {
  name: 'dlog',
  components: {
    SideMenu
  }
}
</script>

<style>
::-webkit-scrollbar {
  display: none;
}

body {
  -webkit-app-region: drag
}
.wrapper {
  height: 100vh;
  padding: 60px 80px;
  width: 100vw;
}

.bg-blue-grey-700 {
  height: 100vh;
  width: 20vh!important;
  background-color: #37474f!important
}

</style>
