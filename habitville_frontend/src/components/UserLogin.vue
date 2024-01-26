<template>
  <div class="login-container">
    <h1>Login</h1>
    <form @submit.prevent="submitLogin">
      <div class="form-group">
        <label for="username">Username:</label>
        <input type="text" id="username" v-model="username" required />
      </div>
      <div class="form-group">
        <label for="password">Password:</label>
        <input type="password" id="password" v-model="password" required />
      </div>
      <div class="form-group button-container">
        <button type="submit">Login</button>
      </div>
      <p v-if="errorMessage" class="error-message">{{ errorMessage }}</p>
    </form>
  </div>
</template>

<script>
import { ref } from 'vue';
import { useStore } from 'vuex';
import { useRouter } from 'vue-router';

export default {
  name: 'UserLogin',
  setup() {
    const store = useStore();
    const router = useRouter();
    const username = ref('');
    const password = ref('');
    const errorMessage = ref(null);

    const submitLogin = async () => {
      try {
        await store.dispatch('login', {
          username: username.value,
          password: password.value
        });
        router.push('/habits');
      } catch (error) {
        errorMessage.value = 'Login failed. Please try again.';
        if (error.response && error.response.data && error.response.data.error) {
          errorMessage.value = error.response.data.error;
        }
      }
    };

    return {
      username,
      password,
      errorMessage,
      submitLogin
    };
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

.button-container {
  display: flex;
  justify-content: center;
}

.form-group button {
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
