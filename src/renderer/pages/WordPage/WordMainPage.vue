<template>
    <div class="wrapper">
        <div class="row mb-2">
          <h1>Word</h1>
          <div class="btn-group ml-1">
            <button type="button" class="btn btn-floating btn-danger"><img class="icon" src="/static/icons/add.png"></button>
          </div>
        </div>
        <div class="shadow p-3 mb-5 bg-white rounded">
          <div class="form-group">
            <label for="exampleInputEmail1">Email address</label>
            <input type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" placeholder="Enter email">
            <small id="emailHelp" class="form-text text-muted">We'll never share your email with anyone else.</small>
          </div>
        </div>
        <div class="shadow p-3 mb-5 bg-white rounded">
          <div class="form-group">
            <label for="exampleInputEmail1">Email address</label>
            <input type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" placeholder="Enter email">
            <small id="emailHelp" class="form-text text-muted">We'll never share your email with anyone else.</small>
          </div>
        </div>
    </div>
</template>

<script>
export default {
  name: 'word-mainpage'
}
</script>

<style scoped>
  div.wrapper {
    background-color: #97a3aa!important
  }
  img.icon {
    width: 30px;
    height: auto;
  }
</style>


