import { reactive } from 'vue';

export const store = reactive({
  isAuthenticated: localStorage.getItem('isAuthenticated') === 'true',
});

export function setAuth(isAuth) {
  localStorage.setItem('isAuthenticated', isAuth);
  store.isAuthenticated = isAuth === 'true';
}
