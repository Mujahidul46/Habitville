<template>
  <div id="app">
    <NavBar />
    <router-view />
  </div>
</template>

<script>
import NavBar from './components/NavBar.vue'
import axios from 'axios'
import { setAuth } from './store' 

export default {
  name: 'App',
  components: { NavBar },
  created() {
    axios.get('http://127.0.0.1:8000/accounts/verify-session/', { withCredentials: true })
      .then(response => {
        // Update the authentication state based on the response
        setAuth(response.data.isAuthenticated ? 'true' : 'false');
      })
      .catch(() => {
        setAuth('false');
      });
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
