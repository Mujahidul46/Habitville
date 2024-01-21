<template>
    <nav class="navbar">
      <!-- Links available (not logged in) -->
      <router-link to="/">Home</router-link>
      <router-link to="/signup">Signup</router-link>
      <router-link to="/login">Login</router-link>
  
      <!-- TO DO: add links here for authenticated users -->
    </nav>
  </template>
  
  <script>
  export default {
    name: 'NavBar',
  };
  </script>
  
  <style scoped>
    .navbar {
      background-color: #a2e28b;
      padding: 1rem;
      display: flex;
      justify-content: center;
    }
  
    .navbar a, .navbar button {
      margin: 0 10px;
      color: rgb(0, 0, 0);
      text-decoration: none;
      cursor: pointer;
      background: none;
      border: none;
      padding: 0;
      font: inherit;
    }
  
    .navbar a.router-link-exact-active,
    .navbar a:hover {
      text-decoration: underline;
    }
  </style>
  