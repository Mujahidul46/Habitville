<template>
  <div id="app">
    <NavBar />
    <router-view />
  </div>
</template>

<script>
import NavBar from './components/NavBar.vue'
import store from './store'

export default {
  name: 'App',
  components: {
    NavBar
  },
  created() {
    store.dispatch('checkAuth');
  }
}
</script>

<style>
html, body {
  height: 100%;
  margin: 0;
  padding: 0;
}

#app {
  min-height: 100%;
  background-color: hsl(104, 67%, 77%);
  color: #333;
  font-family: 'Open Sans', Arial, sans-serif;
}
</style>
