<template>
  <div id="app" class="row">
      <div id="side-menu-div" class="col-3 bg-blue-grey-700">
        <side-menu></side-menu>
      </div>
      <div id="content" class="col-9 px-0">
        <scrolly class="foo" :style="{ width: '75.3vw', height: '98vh' }">
          <scrolly-viewport>
            <!-- Your contents here -->
            <router-view></router-view>
          </scrolly-viewport>
          <scrolly-bar axis="y"></scrolly-bar>
        </scrolly>
      </div>
  </div>
</template>

<script>
import { Scrolly, ScrollyViewport, ScrollyBar } from 'vue-scrolly'
import SideMenu from '@/pages/CommonPage/SideMenu'
export default {
  name: 'dlog',
  components: {
    SideMenu,
    Scrolly,
    ScrollyViewport,
    ScrollyBar
  }
}
</script>

<style>
::-webkit-scrollbar {
  display: none;
}
img.icon {
  width: 30px;
  height: auto;
}

body {
  -webkit-app-region: drag;
  background-color: #97a3aa!important
}
.wrapper {
  padding: 50px 50px;
  height: 600px;
  width: 1000px;
}

.bg-blue-grey-700 {
  height: 100vh;
  width: 20vh!important;
  background-color: #37474f!important
}

</style>
