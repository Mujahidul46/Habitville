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
      <div class="form-group">
        <label for="confirmPassword">Confirm Password</label>
        <input type="password" id="confirmPassword" v-model="confirmPassword" required>
      </div>
      <div class="form-group button-container">
        <button type="submit">Sign Up</button>
      </div>
    </form>
    <p v-if="formError" class="error-message">{{ formError }}</p>
  </div>
</template>

<script>
  import axios from 'axios';

  export default {
    name: 'UserSignup',
    data() {
      return {
        username: '',
        password: '',
        confirmPassword: '',
        formError: '', 
      };
    },
    methods: {
      handleSubmit() {
        this.formError = '';

        // Username checks
        if(this.username.length < 3) {
          this.formError = "Username must be at least 3 characters long.";
          return;
        }
        if(!this.username.match(/^[a-zA-Z0-9._]+$/)) {
          this.formError = "Username can only contain alphanumeric characters, periods, and underscores.";
          return;
        }
        if(!isNaN(this.username)) {
          this.formError = "Username cannot be purely numerical.";
          return;
        }
        // Password checks
        if(this.password.length < 6) {
          this.formError = "Password must be at least 6 characters long.";
          return;
        }

        if(this.password === this.username) {
          this.formError = "Password cannot be the same as the username.";
          return;
        }
        if(this.password !== this.confirmPassword) {
          this.formError = "Passwords do not match.";
          return;
        }

        const userData = {
          username: this.username,
          password: this.password
        };
        
        // Post request to server with user data
        axios.post('http://127.0.0.1:8000/accounts/signup/', userData)
          .then(response => {
            // TODO: Redirect to the login page or dashboard
            console.log(response.data);
          })
          .catch(error => {
            console.error(error);
            if (error.response) {
              // checks if username already exists
              if (error.response.status === 400 && error.response.data.username_exists) {
                this.formError = error.response.data.message;
              } else {
                this.formError = error.response.data.detail || 'An error occurred. Please try again later.';
              }
            } else { // likely network issue/server down
              this.formError = 'Cannot reach the server. Please check your network connection.';
            }
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
