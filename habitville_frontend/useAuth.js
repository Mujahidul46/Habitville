// useAuth.js
import { ref } from 'vue';

const isAuthenticated = ref(!!localStorage.getItem('userToken'));

export function useAuth() {
  function login(token) {
    localStorage.setItem('userToken', token);
    isAuthenticated.value = true;
  }

  function logout() {
    localStorage.removeItem('userToken');
    isAuthenticated.value = false;
  }

  return {
    isAuthenticated,
    login,
    logout
  };
}
