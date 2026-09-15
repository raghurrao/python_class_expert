# Day 15-16: Vue Router Introduction

Welcome to Week 3! Up until now, our app has lived on a single page. Real-world applications have multiple pages (e.g., Home, About, User Profile). **Vue Router** is the official router for Vue.js.

## 1. Installation
In a standard Vite project, you can install it via:
```bash
npm install vue-router@4
```

## 2. Basic Setup
Create a `router.js` file:
```javascript
import { createRouter, createWebHistory } from 'vue-router'
import HomeView from './views/HomeView.vue'
import AboutView from './views/AboutView.vue'

const routes = [
  { path: '/', component: HomeView },
  { path: '/about', component: AboutView },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router
```

In `main.js`:
```javascript
import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

const app = createApp(App)
app.use(router)
app.mount('#app')
```

## 3. RouterView and RouterLink
In your `App.vue`, you need a place to render the current route's component, and links to navigate between them.
- `<router-view>` acts as a placeholder for the component matching the URL.
- `<router-link>` acts as an anchor `<a>` tag that prevents full page reloads.

```vue
<template>
  <nav>
    <router-link to="/">Home</router-link>
    <router-link to="/about">About</router-link>
  </nav>

  <main>
    <router-view /> <!-- Components render here! -->
  </main>
</template>
```

## 4. Dynamic Routing
You can match dynamic segments in the URL (like an ID):
```javascript
{ path: '/users/:id', component: UserProfile }
```
Inside `UserProfile.vue`, you can access the ID using the `useRoute` composable:
```vue
<script setup>
import { useRoute } from 'vue-router'
const route = useRoute()
console.log(route.params.id)
</script>
```

---

## 🚀 Your Assignment
1. Install `vue-router` in your `vue-playground`.
2. Set up three views: `HomeView.vue`, `ProductsView.vue`, and `ProductDetailView.vue`.
3. Add navigation links to `App.vue`.
4. Make `ProductDetailView` use a dynamic route (e.g., `/products/:id`) and display the `id` on the page.
