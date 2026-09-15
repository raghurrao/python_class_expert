# Day 17-18: Navigation Guards & Route Meta

## 1. Programmatic Navigation
Sometimes you need to navigate the user via code (e.g., after they successfully log in). You can use the `useRouter` composable.

*(Note: `useRoute` is for getting information about the current route, while `useRouter` is for triggering navigation).*

```vue
<script setup>
import { useRouter } from 'vue-router'
const router = useRouter()

function login() {
  // perform login...
  router.push('/dashboard')
}
</script>
```

## 2. Navigation Guards
Navigation guards allow you to intercept routing (before it happens, or after) to redirect the user or cancel the navigation. This is primarily used for **Authentication**.

```javascript
router.beforeEach((to, from) => {
  const isAuthenticated = checkAuth() 

  // If the user is not authenticated and trying to access a protected route
  if (to.name !== 'Login' && !isAuthenticated) {
    return { name: 'Login' } // Redirect to login
  }
})
```

## 3. Route Meta Fields
How do you know if a route requires authentication? You can attach custom data to a route using the `meta` property.

```javascript
const routes = [
  {
    path: '/dashboard',
    component: DashboardView,
    meta: { requiresAuth: true }
  }
]
```

Then in your guard:
```javascript
router.beforeEach((to, from) => {
  if (to.meta.requiresAuth && !isAuthenticated) {
    return '/login'
  }
})
```

---

## 🚀 Your Assignment
1. Add a `meta: { requiresAuth: true }` field to your `ProductsView` from the previous lesson.
2. Implement a global `beforeEach` navigation guard in your router.
3. Fake an authentication state (e.g., `let isLoggedIn = false`).
4. If a user tries to access `/products` while `isLoggedIn` is false, redirect them to a new `LoginView`.
