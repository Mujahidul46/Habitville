import { createStore } from 'vuex';
import axios from 'axios';

export default createStore({
  state: {
    isAuthenticated: false,
    username: null,
  },
  mutations: {
    setAuth(state, { isAuthenticated, username }) {
      state.isAuthenticated = isAuthenticated;
      state.username = username;
    }
  },
  actions: {
    async login({ commit }, credentials) {
      let response = await axios.post('http://127.0.0.1:8000/accounts/login/', credentials);
      localStorage.setItem('auth', JSON.stringify({ username: response.data.username }));
      commit('setAuth', { isAuthenticated: true, username: response.data.username });
    },
    logout({ commit }) {
      localStorage.removeItem('auth');
      commit('setAuth', { isAuthenticated: false, username: null });
    },
    checkAuth({ commit }) {
      let auth = localStorage.getItem('auth');
      if (auth) {
        auth = JSON.parse(auth);
        commit('setAuth', { isAuthenticated: true, username: auth.username });
      } else {
        commit('setAuth', { isAuthenticated: false, username: null });
      }
    }
  },
  getters: {
    isAuthenticated(state) {
      return state.isAuthenticated;
    },
    username(state) {
      return state.username;
    }
  }
});
