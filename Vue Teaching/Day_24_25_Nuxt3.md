# Day 24-25: Introduction to Nuxt 3

Nuxt is the leading framework *built on top of Vue*. If you want to build production-ready Vue applications with SEO capabilities, Nuxt is the way to go.

## 1. Why Nuxt?
A standard Vite + Vue app is a Single Page Application (SPA). This means the server sends an empty HTML file, and the browser builds the DOM using JavaScript. This is bad for SEO and initial load times on slow devices.

Nuxt provides **Server-Side Rendering (SSR)**. The server fully renders the Vue components into HTML before sending them to the browser. 

Nuxt also provides:
- Auto-imports for components, composables, and Vue APIs (no more `import { ref } from 'vue'`).
- File-based routing (no need for a `router.js` file, just put files in a `pages/` directory).
- Powerful data-fetching utilities like `useFetch`.

## 2. Setting up Nuxt
To start a new Nuxt project (try this in a new terminal, outside of your vue-playground):
```bash
npx nuxi@latest init my-nuxt-app
cd my-nuxt-app
npm install
npm run dev
```

## 3. File-Based Routing
In Nuxt, if you create a `pages/` directory:
- `pages/index.vue` maps to `/`
- `pages/about.vue` maps to `/about`
- `pages/products/[id].vue` maps to dynamic routes like `/products/123`.

## 4. Universal Data Fetching
Nuxt provides `useFetch` to fetch data on the server during SSR, and automatically pass that data to the client to prevent double-fetching.

```vue
<!-- pages/index.vue -->
<script setup>
const { data: users, pending } = await useFetch('https://jsonplaceholder.typicode.com/users')
</script>

<template>
  <div v-if="pending">Loading...</div>
  <div v-else>
    <div v-for="user in users" :key="user.id">{{ user.name }}</div>
  </div>
</template>
```

---

## 🚀 Your Assignment
1. Initialize a new Nuxt 3 project on your machine.
2. Create an `app.vue` file that uses `<NuxtPage />` (which is Nuxt's equivalent of `<router-view>`).
3. Create a `pages/index.vue` and a `pages/about.vue`. Navigate between them using `<NuxtLink to="/about">` (Nuxt's `<router-link>`).
