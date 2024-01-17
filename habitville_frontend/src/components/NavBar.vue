<template>
    <nav class="navbar">
      <router-link to="/">Home</router-link>
      <router-link to="/signup">Signup</router-link>
      <span class="inactive-link">Login</span> <!-- Not clickable for now -->
    </nav>
</template>
  
<script>
    export default {
        name: 'NavBar'
    };
</script>

<style scoped>
    .navbar {
    background-color: #2ecc71; /* Green background */
    padding: 1rem;
    display: flex;
    justify-content: center;
    }

    .navbar a,
    .navbar .inactive-link {
    margin: 0 10px;
    color: white;
    text-decoration: none;
    cursor: pointer;
    }

    .navbar a.router-link-exact-active,
    .navbar a:hover {
    text-decoration: underline;
    }

    .inactive-link {
    color: #cccccc;
    cursor: default;
    }
</style>
