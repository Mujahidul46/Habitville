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
      <div class="form-group button-container">
        <button type="submit">Sign Up</button>
      </div>
    </form>
  </div>
</template>

<script>
  import axios from 'axios';

  export default {
    name: 'UserSignup',
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
          })
          .catch(error => {
            console.error(error);
          });
      }
    }
  };
</script>

<style scoped>
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
  margin-bottom: 5px;
}

.form-group input {
  width: 100%;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 4px;
}

.button-container {
  display: flex;
  justify-content: center; 
  margin-bottom: 15px;
}

.form-group button {
  width: 25%;
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
