<template>
    <div class="wrapper">
        <div class="row mb-2">
          <h1>Word</h1>
          <div class="btn-group ml-1">
            <button type="button" class="btn btn-floating btn-danger mr-2" @click="fnadd"><img class="icon" src="/static/icons/add.png"></button>
            <button type="button" class="btn btn-floating btn-success" @click="fnadd"><img class="icon" src="/static/icons/upload-arrow.png"></button>
          </div>
        </div>
        <shadowbox :items="worditems" ></shadowbox>
    </div>
</template>

<script>
import Shadowbox from '@/components/word/Shadowbox'
export default {
  name: 'word-mainpage',
  data () {
    return {
      worditems: []
    }
  },
  components: {
    Shadowbox
  },
  methods: {
    fnadd () {
      this.worditems.push({})
    }
  }
}
</script>

<style scoped>
  img.icon {
    width: 30px;
    height: auto;
  }
</style>


