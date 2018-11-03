<template>
  <div class="wrapper">
    <h6>__dirname__ : {{this.statusinfo.__dirname__}}</h6>
    <h6>__parentdir__ : {{this.statusinfo.__parentdir__}}</h6>
    <h6>realpath : {{this.statusinfo.realpath}}</h6>
    <h6>__name__ : {{this.statusinfo.__name__}}</h6>
  </div>
</template>

<script>
export default {
  name: 'landing-page',
  data () {
    return {
      statusinfo: {}
    }
  },
  async created () {
    this.statusinfo = await this.$pyrouterFn('dloginfo', JSON.stringify({dos: 'dos'}))
    console.log(this.statusinfo)
  }
}
</script>

<style>
</style>
