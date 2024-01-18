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

router.beforeEach((to, from, next) => { // Ensures that user can't bypass login by going to /habits url. It redirects user to login.
  const userIsAuthenticated = localStorage.getItem('userToken') !== null;
  console.log('Routing to:', to.name); // Debug statement
  console.log('User is authenticated:', userIsAuthenticated); // Debug statement

  if (to.path === '/habits' && !userIsAuthenticated) {
    console.log('User is not authenticated, redirecting to UserLogin'); // Debug statement
    next({ name: 'UserLogin' });
  } else {
    console.log('Proceeding to:', to.name); // Debug statement
    next();
  }
});

export default router;