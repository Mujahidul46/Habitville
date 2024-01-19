<template>
  <nav class="navbar">
    <!-- Links only when the user is not logged in -->
    <template v-if="!isAuthenticated">
      <router-link to="/">Home</router-link>
      <router-link to="/signup">Signup</router-link>
      <router-link to="/login">Login</router-link>
    </template>

    <!-- Links only when the user is logged in -->
    <template v-if="isAuthenticated">
      <router-link to="/habits">Habit Tracker</router-link>
      <!-- Add other links as needed -->

      <!-- Logout button -->
      <button @click="performLogout">Logout</button>
    </template>
  </nav>
</template>

<script>
import { useAuth } from '../../useAuth.js';
import { useRouter } from 'vue-router';

export default {
  name: 'NavBar',
  setup() {
    const router = useRouter(); 
    const { isAuthenticated, logout } = useAuth();

    const performLogout = () => {
      logout();
      router.push('/'); // redirects to home page after logout
    };

    return {
      isAuthenticated,
      performLogout, 
    };
  },
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
  .navbar a:hover,
  .navbar button:hover {
    text-decoration: underline;
  }

  button {
    cursor: pointer;
    color: rgb(0, 0, 0);
    background-color: transparent;
    border: none;
    padding: 0;
    font-size: 1rem;
  }
</style>
