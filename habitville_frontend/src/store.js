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
      commit('setAuth', { isAuthenticated: true, username: response.data.username });
    },
    logout({ commit }) {
      commit('setAuth', { isAuthenticated: false, username: null });
    },
    checkAuth({ commit }) {
      const username = localStorage.getItem('username');
      const isAuthenticated = !!username;
      commit('setAuth', { isAuthenticated, username });
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
