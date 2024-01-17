<template>
    <nav class="navbar">
      <router-link to="/">Home</router-link>
      <router-link to="/signup">Signup</router-link>
      <router-link to="/login">Login</router-link>
    </nav>
  </template>
  
  <script>
  export default {
      name: 'NavBar'
  };
  </script>
  
  <style scoped>
    .navbar {
      background-color: #a2e28b; 
      padding: 1rem;
      display: flex;
      justify-content: center;
    }
  
    .navbar a {
      margin: 0 10px;
      color: rgb(0, 0, 0);
      text-decoration: none;
      cursor: pointer;
    }
  
    .navbar a.router-link-exact-active,
    .navbar a:hover {
      text-decoration: underline;
    }
  </style>
  