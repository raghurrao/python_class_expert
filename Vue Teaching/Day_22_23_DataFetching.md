# Day 22-23: Data Fetching & Async Components

Welcome to Week 4! We are focusing on real-world patterns, starting with fetching data from a backend server.

## 1. Fetching Data on Mount
The most common way to fetch data is inside the `onMounted` lifecycle hook.

```vue
<script setup>
import { ref, onMounted } from 'vue'

const users = ref([])
const loading = ref(false)

onMounted(async () => {
  loading.value = true
  try {
    const res = await fetch('https://jsonplaceholder.typicode.com/users')
    users.value = await res.json()
  } catch (error) {
    console.error(error)
  } finally {
    loading.value = false
  }
})
</script>

<template>
  <p v-if="loading">Loading users...</p>
  <ul v-else>
    <li v-for="user in users" :key="user.id">{{ user.name }}</li>
  </ul>
</template>
```

## 2. Suspense (Experimental but awesome)
Vue 3 has a `<Suspense>` built-in component that orchestrates async dependencies in your component tree. This allows you to use top-level `await` in your `<script setup>`!

```vue
<!-- UserList.vue -->
<script setup>
// Look, no onMounted! Top-level await is allowed here.
const res = await fetch('https://jsonplaceholder.typicode.com/users')
const users = await res.json()
</script>
```

In the parent component, wrap it in `<Suspense>`:
```vue
<template>
  <Suspense>
    <!-- component with async setup -->
    <UserList />

    <!-- loading state via #fallback slot -->
    <template #fallback>
      Loading...
    </template>
  </Suspense>
</template>
```

## 3. Async Components
If you have a heavy component (e.g., a massive chart library) that you don't need immediately, you can lazy-load it using `defineAsyncComponent`.

```javascript
import { defineAsyncComponent } from 'vue'

const HeavyChart = defineAsyncComponent(() =>
  import('./components/HeavyChart.vue')
)
```
This splits the JavaScript bundle, improving initial page load speed.

---

## 🚀 Your Assignment
1. Create a `PostsView.vue` component.
2. Fetch a list of posts from `https://jsonplaceholder.typicode.com/posts` using top-level `await`.
3. Render the list of posts.
4. Wrap your `PostsView` in a `<Suspense>` boundary in `App.vue` and provide a nice fallback loading message.
