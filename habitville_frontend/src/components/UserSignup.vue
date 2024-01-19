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
import { ref } from 'vue';
import axios from 'axios';
import { useRouter } from 'vue-router';
import { useAuth } from '../../useAuth.js';

export default {
  name: 'UserSignup',
  setup() {
    const router = useRouter(); 
    const { login } = useAuth(); 
    const username = ref('');
    const password = ref('');
    const confirmPassword = ref('');
    const formError = ref('');

    const handleSubmit = async () => {
      formError.value = '';

      // Form validation - Username checks
      if(username.value.length < 3) {
        formError.value = "Username must be at least 3 characters long.";
        return;
      }
      if(!username.value.match(/^[a-zA-Z0-9._]+$/)) {
        formError.value = "Username can only contain alphanumeric characters, periods, and underscores.";
        return;
      }
      if(!isNaN(username.value)) {
        formError.value = "Username cannot be purely numerical.";
        return;
      }
      // Form validation - Password checks
      if(password.value.length < 6) {
        formError.value = "Password must be at least 6 characters long.";
        return;
      }

      if(password.value === username.value) {
        formError.value = "Password cannot be the same as the username.";
        return;
      }
      if(password.value !== confirmPassword.value) {
        formError.value = "Passwords do not match.";
        return;
      }

      try {
        const response = await axios.post('http://127.0.0.1:8000/accounts/signup/', {
          username: username.value,
          password: password.value
        });
        if (response.data.token) {
          login(response.data.token); 
          router.push('/habits'); // Redirects to the habits page immediately after signing up - skips unnecessary login
        } else {
          console.error('No token returned from server');
          formError.value = 'Signup successful, but could not log you in automatically.';
        }
      } catch (error) {
        console.error(error);
        if (error.response) {
          // checks if username already exists
          if (error.response.status === 400 && error.response.data.username_exists) {
            formError.value = error.response.data.message;
          } else {
            formError.value = error.response.data.detail || 'An error occurred. Please try again later.';
          }
        } else { // likely network issue/server down
          formError.value = 'Cannot reach the server. Please check your network connection.';
        }
      }
    };

    return {
      username,
      password,
      confirmPassword,
      formError,
      handleSubmit,
    };
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
