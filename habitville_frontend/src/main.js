import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import axios from 'axios';

// Configures Axios to send cookies
axios.defaults.withCredentials = true;

createApp(App).use(router).mount('#app')