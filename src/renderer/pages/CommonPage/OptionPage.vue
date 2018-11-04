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
          <div class="input-group">
            <span class="form-control">{{this.options.tempdir}}</span>
            <div class="input-group-prepend">
              <button class="btn btn-outline-info" @click="$refs.gettempdir.click()">찾기</button>
            </div>
            <input type="file" class="form-control" style="display:none" ref="gettempdir" @change="getdir" id="tempdir"  webkitdirectory directory multiple/>
          </div>
      </div>
      <div class="form-group">
          <label for="">Export Directory</label>
          <div class="input-group">
            <span class="form-control">{{this.options.exportdir}}</span>
            <div class="input-group-append">
              <button class="btn btn-outline-info" @click="$refs.getexportdir.click()">찾기</button>
            </div>
            <input type="file" class="form-control" style="display:none" ref="getexportdir" @change="getdir" id="exportdir"  webkitdirectory directory multiple/>
          </div>
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
        file: `${this.$curdirname}conf\\options.json`,
        dir: `${this.$curdirname}conf`
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
      const data = fs.readFileSync(this.json.file, 'utf8')
      this.options = JSON.parse(data)
    } catch (error) {
      console.log('no such dir')
      fs.mkdirSync(this.json.dir)
      fs.writeFileSync(this.json.file, JSON.stringify({}), 'utf8')
    }
  },
  methods: {
    saveConf: function () {
      try {
        console.log(this.json.file)
        fs.accessSync(this.json.file, fs.constants.F_OK)
      } catch (error) {
        console.log('no such dir')
        fs.mkdirSync(this.json.dir)
      } finally {
        fs.writeFileSync(this.json.file, JSON.stringify(this.options), 'utf8')
      }
    },
    getdir: function (e) {
      console.log(e)
      console.log(this)
      if (e.target.id === 'tempdir') {
        this.options.tempdir = e.target.files[0].path
      } else if (e.target.id === 'exportdir') {
        this.options.exportdir = e.target.files[0].path
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

