<template>
  <div class="wrapper">
    <h1>Home</h1>
  </div>
</template>

<script>
export default {
  name: 'landing-page',
  created () {
    this.$PythonShell.runString('x=1+1;print(x)', null, function (err, results) {
      if (err) throw err
      alert(results)
    })
  }
}
</script>

<style>
</style>
