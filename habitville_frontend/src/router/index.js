import { createRouter, createWebHistory } from 'vue-router';
import UserSignup from '@/components/UserSignup.vue';


const routes = [
  {
    path: '/signup',
    name: 'UserSignup',
    component: UserSignup,
  },
  // add more routes here
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
