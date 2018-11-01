<template>
  <b-nav vertical id="side-menu">
    <b-nav-item>주간업무보고서 작성</b-nav-item>
    <b-nav-item>기능 구상중..</b-nav-item>
    <b-nav-item>기능 구상중..</b-nav-item>
  </b-nav>
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
  #side-menu {
    background: rgba(22, 124, 128, 1);
    padding-top: 10px;
    width: 100vw;
  }
  #side-menu > li > a {
    color: white
  }
  #side-menu > li > a:hover {
    background: rgb(77, 126, 128)
  }
</style>

