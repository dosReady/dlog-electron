<template>
    <div class="wrapper">
        <div class="row mb-2">
          <h1>Word</h1>
          <div class="btn-group ml-1">
            <button type="button" class="btn btn-floating btn-danger mr-2" @click="fnadd"><img class="icon" :src="icon.add"></button>
            <button type="button" class="btn btn-floating btn-success" @click="fnexport"><img class="icon" :src="icon.upload_arrow"></button>
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
      worditems: [],
      icon: {
        add: require('@/static/icons/add.png'),
        upload_arrow: require('@/static/icons/upload-arrow.png')
      }
    }
  },
  components: {
    Shadowbox
  },
  methods: {
    fnadd () {
      this.worditems.push({})
    },
    async fnexport () {
      const val = await this.$pyrouterFn('wordcreate')
      console.log(val)
    }
  }
}
</script>

<style scoped>
</style>


