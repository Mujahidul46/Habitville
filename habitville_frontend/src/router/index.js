import { createRouter, createWebHistory } from 'vue-router';
import HomePage from '@/components/HomePage.vue';
import UserSignup from '@/components/UserSignup.vue';
import UserLogin from '@/components/UserLogin.vue';
import HabitTracker from '@/components/HabitTracker.vue';
import store from '@/store'; 

const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: '/',
      name: 'HomePage',
      component: HomePage
    },
    {
      path: '/signup',
      name: 'UserSignup',
      component: UserSignup
    },
    {
      path: '/login',
      name: 'UserLogin',
      component: UserLogin
    },
    {
      path: '/habits',
      name: 'HabitTracker',
      component: HabitTracker,
      meta: { requiresAuth: true }
    },
  ]
});

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requiresAuth)) {
    if (!store.getters.isAuthenticated) {
      next({ name: 'UserLogin' });
    } else {
      next();
    }
  } else {
    next();
  }
});

export default router;
