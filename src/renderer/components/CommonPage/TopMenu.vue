<template>
    <header>
        <ul>
            <li><a href="#">Home</a></li>
            <li><a href="#">HTML</a></li>
            <li><a href="#">CSS</a></li>
            <ul style="float:right; list-style-type:none;">
                <li><a @click="fnminimizing">─</a></li>
                 <li><a @click="fnunmaximizing">ㅁ</a></li>
                <li><a @click="fnmaximizing">ㅁ</a></li>
                <li><a @click="fnclose">Ⅹ</a></li>
            </ul>
        </ul>
    </header>
</template>

<script>
export default {
  name: 'top-menu',
  methods: {
    fnmaximizing () {
      let win = this.$electron.remote.getCurrentWindow()
      win.maximize()
    },
    fnunmaximizing () {
      let win = this.$electron.remote.getCurrentWindow()
      win.unmaximize()
    },
    fnminimizing () {
      let win = this.$electron.remote.getCurrentWindow()
      win.minimize()
    },
    fnclose () {
      let win = this.$electron.remote.getCurrentWindow()
      win.close()
    }
  }
}
</script>

<style scoped>
    header {
      -webkit-app-region: drag;
    }
    ul {
        background:
        radial-gradient(
        ellipse at top left,
        rgba(60, 179, 113, 1) 40%,
        rgba(60, 179, 113, .9) 100%
        );
        list-style-type: none;
        margin: 0;
        padding: 0;
        overflow: hidden;
    }
    li { float: left; }
    li a {
        display: block;
        color: #000000;
        padding: 8px;
        text-decoration: none;
        text-align: center;
        font-weight: bold;
        -webkit-app-region: no-drag;
        cursor: pointer;
    }
    li a.current {
        background: white;
    }
    li a:hover:not(.current) {
        background: white;
    }
</style>

