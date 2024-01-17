<template>
    <div class="login-container">
      <h1>Login</h1>
      <form @submit.prevent="submitLogin">
        <div class="form-group">
          <label for="username">Username</label>
          <input type="text" id="username" v-model="username" required />
        </div>
        <div class="form-group">
          <label for="password">Password</label>
          <input type="password" id="password" v-model="password" required />
        </div>
        <div class="form-group">
          <button type="submit">Login</button>
        </div>
        <p v-if="errorMessage" class="error-message">{{ errorMessage }}</p>
      </form>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    name: 'UserLogin',
    data() {
      return {
        username: '',
        password: '',
        errorMessage: ''
      };
    },
    methods: {
      async submitLogin() {
        try {
          const response = await axios.post('http://127.0.0.1:8000/accounts/login/', {
            username: this.username,
            password: this.password
          });
          if (response.status === 200) {
            this.$router.push('/habits'); 
          }
        } catch (error) {
          if (error.response && error.response.status === 404) {
            this.errorMessage = 'Invalid username or password';
          } else {
            this.errorMessage = 'An error occurred. Please try again later.';
          }
        }
      }
    }
  };
  </script>
  
  <style scoped>
  .login-container {
    max-width: 300px;
    margin: auto;
    padding: 20px;
  }
  
  .form-group {
    margin-bottom: 15px;
  }
  
  .form-group label {
    display: block;
    margin-bottom: 5px;
  }
  
  .form-group input {
    width: 100%;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 4px;
  }
  
  .form-group button {
    width: 100%;
    padding: 10px;
    background-color: #5cb85c;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
  }
  
  .form-group button:hover {
    background-color: #4cae4c;
  }
  
  .error-message {
    color: red;
    text-align: center;
  }
  </style>
  