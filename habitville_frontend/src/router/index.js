import { createRouter, createWebHistory } from 'vue-router';
import HomePage from '@/components/HomePage.vue';
import UserSignup from '@/components/UserSignup.vue';
import UserLogin from '@/components/UserLogin.vue';
import HabitTracker from '@/components/HabitTracker.vue';

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
      component: HabitTracker
    },
  ]
});

router.beforeEach((to, from, next) => {
  const userIsAuthenticated = !!localStorage.getItem('userToken');

  if (!userIsAuthenticated && to.name === 'HabitTracker') {
    next({ name: 'UserLogin' });
  } else if (userIsAuthenticated && (to.name === 'UserLogin' || to.name === 'UserSignup')) {
    next({ name: 'HabitTracker' });
  } else {
    next();
  }
});

export default router;