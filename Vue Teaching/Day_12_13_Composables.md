# Day 12-13: Composables & Advanced Composition API

## 1. What is a Composable?
In Vue, a "composable" is a function that leverages Vue's Composition API to encapsulate and reuse **stateful logic**. 

In Vue 2 (Options API), reusing logic often involved Mixins, which were prone to naming collisions and unclear data sources. The Composition API solves this elegantly.

```javascript
// useMouse.js
import { ref, onMounted, onUnmounted } from 'vue'

export function useMouse() {
  const x = ref(0)
  const y = ref(0)

  function update(event) {
    x.value = event.pageX
    y.value = event.pageY
  }

  onMounted(() => window.addEventListener('mousemove', update))
  onUnmounted(() => window.removeEventListener('mousemove', update))

  return { x, y }
}
```

Usage in a component:
```vue
<script setup>
import { useMouse } from './useMouse.js'

const { x, y } = useMouse()
</script>

<template>
  Mouse position is at: {{ x }}, {{ y }}
</template>
```

## 2. Template Refs
Sometimes you need direct access to an underlying DOM element or a child component instance. You can do this using `ref` in the template.

```vue
<script setup>
import { ref, onMounted } from 'vue'

const inputElement = ref(null)

onMounted(() => {
  inputElement.value.focus() // Focus the input when the component mounts
})
</script>

<template>
  <input ref="inputElement" />
</template>
```

## 3. Lifecycle Hooks
Vue components go through a lifecycle (created, mounted, updated, unmounted). You can hook into these stages.
- `onMounted()`: Called after the component has been mounted to the DOM.
- `onUpdated()`: Called after the component has updated its DOM tree due to a reactive state change.
- `onUnmounted()`: Called after the component has been unmounted. (Important for cleanup!)

---

## 🚀 Your Assignment
1. Create a `useFetch` composable that takes a URL, performs a `fetch` request, and returns `{ data, error, isPending }`.
2. Use this composable in a component to fetch data from a public API (like `https://jsonplaceholder.typicode.com/users`) and display it.
