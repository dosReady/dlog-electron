<template>
  <div class="wrapper">
    <div class="row mb-2">

      <h1>옵션</h1>
      <div class="btn-group ml-1">
        <button type="button" class="btn btn-floating btn-danger mr-2" @click="saveConf"><img class="icon" :src="icon.add"></button>
      </div>
    </div>

    <div class="shadow p-3 mb-5 bg-white rounded">
      <div class="form-group">
          <label for="">Template directory</label>
          <input type="text" class="form-control" placeholder="Template directory" v-model="options.tempdir">
      </div>
      <div class="form-group">
          <label for="">Export Directory</label>
          <input type="text" class="form-control" placeholder="Export Directory" v-model="options.exportdir">
      </div>
    </div>
    
  </div>
</template>

<script>
import fs from 'fs'

export default {
  name: 'option-page',
  data () {
    return {
      json: {
        file: `${this.$curdirname}/conf/options.json`,
        dir: `${this.$curdirname}/conf`
      },
      icon: {
        add: require('@/static/icons/add.png')
      },
      options: {
        tempdir: '',
        exportdir: ''
      }
    }
  },
  created () {
    try {
      console.log(this.json.file)
      fs.accessSync(this.json.file, fs.constants.F_OK)
    } catch (error) {
      console.log('no such dir')
      fs.mkdirSync(this.json.dir)
      fs.writeFileSync(this.json.file, null, 'utf8')
    } finally {
      const data = fs.readFileSync(this.json.file, 'utf8')
      this.options = JSON.parse(data)
    }
  },
  methods: {
    saveConf: function () {
      try {
        console.log(this.json.file)
        fs.accessSync(this.json.file, fs.constants.F_OK)
      } catch (error) {
        console.log('no such dir')
        fs.mkdirSync(`${this.$curdirname}/conf`)
      } finally {
        fs.writeFileSync(this.json.file, JSON.stringify(this.options), 'utf8')
      }
    }
  }
}
</script>

<style scoped>
 a.nav-link:hover {
   background-color: #454e53!important
 }
</style>

