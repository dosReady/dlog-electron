<template>
  <div class="wrapper">
    <div class="row mb-2">

      <h1>옵션</h1>
      <div class="btn-group ml-1">
        <button type="button" class="btn btn-floating btn-danger mr-2"><img class="icon" :src="icon.add"></button>
      </div>
    </div>

    <div class="shadow p-3 mb-5 bg-white rounded">
      <div class="form-group">
          <label for="">Template directory</label>
          <input type="text" class="form-control" placeholder="Template directory">
      </div>
      <div class="form-group">
          <label for="">Export Directory</label>
          <input type="text" class="form-control" placeholder="Export Directory">
      </div>
    </div>
    
  </div>
</template>

<script>
export default {
  name: 'option-page',
  data () {
    return {
      icon: {
        add: require('@/static/icons/add.png')
      }
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

