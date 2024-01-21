<template>
  <nav class="navbar">
    <!-- Links when the user is not logged in -->
    <template v-if="!isAuthenticated">
      <router-link to="/">Home</router-link>
      <router-link to="/signup">Signup</router-link>
      <router-link to="/login">Login</router-link>
    </template>

    <!-- Links when the user is logged in -->
    <template v-if="isAuthenticated">
      <router-link to="/habits">Habit Tracker</router-link>
      <router-link to="/profile">Profile</router-link>
      <button @click="logout">Logout</button>
    </template>
  </nav>
</template>

<script>
import { store, setAuth } from '@/store'; 

export default {
  name: 'NavBar',
  computed: {
    isAuthenticated() {
      return store.isAuthenticated; 
    }
  },
  methods: {
    logout() {
      setAuth('false'); 
      this.$router.push('/login');     
    }
  }
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
  