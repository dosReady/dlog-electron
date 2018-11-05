<template>
 <div class="nav flex-column nav-pills" id="v-pills-tab" role="tablist" aria-orientation="vertical">
      <router-link class="nav-link text-white" to="/">Home</router-link>
      <router-link class="nav-link text-white" to="/nwmonitor">Network Monitor</router-link>
      <router-link class="nav-link text-white" to="/options">설정</router-link>
  </div>
</template>

<script>
export default {
  name: 'side-menu',
  data () {
    return {
      curwin: this.$electron.remote.getCurrentWindow()
    }
  },
  methods: {
  }
}
</script>

<style scoped>
 a.nav-link:hover {
   background-color: #454e53!important
 }
</style>

