<template>
  <header>
  <b-navbar toggleable="md" type="dark" variant="info">
    <b-navbar-brand href="#">로고</b-navbar-brand>
    <b-collapse is-nav id="nav_collapse">
      <!-- Right aligned nav items -->
      <b-navbar-nav class="ml-auto">
        <b-nav-item href="#" @click="fnminimizing">축소</b-nav-item>
        <b-nav-item href="#" @click="fnmaximizing">확대</b-nav-item>
        <b-nav-item href="#" @click="fnclose">닫기</b-nav-item>
      </b-navbar-nav>
    </b-collapse>
  </b-navbar>
  </header>
</template>

<script>
export default {
  name: 'top-menu',
  data () {
    return {
      curwin: this.$electron.remote.getCurrentWindow()
    }
  },
  methods: {
    fnmaximizing () {
      this.curwin.maximize()
    },
    fnunmaximizing () {
      this.curwin.unmaximize()
    },
    fnminimizing () {
      this.curwin.minimize()
    },
    fnclose () {
      this.curwin.close()
    }
  }
}
</script>

<style scoped>
  header {
    -webkit-app-region: drag;
  }
  a.nav-link {
    -webkit-app-region: no-drag;
    color: white!important
  }
</style>

