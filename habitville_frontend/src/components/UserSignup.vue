<template>
    <div class="signup-container">
      <h1>Sign Up</h1>
      <form @submit.prevent="handleSubmit">
        <div class="form-group">
          <label for="username">Username</label>
          <input type="text" id="username" v-model="username" required>
        </div>
        <div class="form-group">
          <label for="password">Password</label>
          <input type="password" id="password" v-model="password" required>
        </div>
        <button type="submit">Sign Up</button>
      </form>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        username: '',
        password: ''
      };
    },
    methods: {
      handleSubmit() {
        const userData = {
          username: this.username,
          password: this.password
        };
        axios.post('http://127.0.0.1:8000/accounts/signup/', userData)
          .then(response => {
            console.log(response.data);
            // Redirect to login or another page upon successful signup
            // this.$router.push('/login');
          })
          .catch(error => {
            console.error(error);
            // Handle errors, such as showing an error message to the user
          });
      }
    }
  };
  </script>
  
  <style scoped>
  /* Add styles for your signup container here */
  .signup-container {
    max-width: 300px;
    margin: auto;
    padding: 20px;
  }
  
  .form-group {
    margin-bottom: 15px;
  }
  
  .form-group label {
    display: block;
  }
  
  .form-group input {
    width: 100%;
    padding: 8px;
    margin-top: 5px;
  }
  
  button {
    width: 100%;
    padding: 10px;
    background-color: #42b983;
    color: white;
    border: none;
    cursor: pointer;
  }
  </style>
  