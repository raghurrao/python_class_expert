# Day 19-20: State Management with Pinia

As your application grows, passing props down 5 levels deep ("prop drilling") becomes a nightmare. For complex apps, we use a Global State Management library. The official recommendation for Vue 3 is **Pinia**.

## 1. Installation & Setup
```bash
npm install pinia
```
In `main.js`:
```javascript
import { createPinia } from 'pinia'
app.use(createPinia())
```

## 2. Defining a Store
Stores are defined using `defineStore()`. A Setup Store (which looks just like a component's `<script setup>`) is highly recommended.

```javascript
// stores/counter.js
import { defineStore } from 'pinia'
import { ref, computed } from 'vue'

export const useCounterStore = defineStore('counter', () => {
  // State
  const count = ref(0)
  
  // Getters (computed)
  const doubleCount = computed(() => count.value * 2)
  
  // Actions (methods)
  function increment() {
    count.value++
  }

  return { count, doubleCount, increment }
})
```

## 3. Using the Store
You can use the store in any component without needing to pass props.

```vue
<script setup>
import { useCounterStore } from '@/stores/counter'
const store = useCounterStore()
</script>

<template>
  <p>Count is: {{ store.count }}</p>
  <p>Double is: {{ store.doubleCount }}</p>
  <button @click="store.increment()">Add 1</button>
</template>
```

*(Note: If you destructure the store, you must use `storeToRefs` to keep reactivity, just like normal reactive objects!)*

---

## 🚀 Your Assignment
1. Install Pinia in your playground.
2. Create an `auth.js` store that holds a reactive boolean `isLoggedIn` and functions to `login()` and `logout()`.
3. Update your Router Navigation Guard from Day 18 to read the `isLoggedIn` state directly from your Pinia store!
