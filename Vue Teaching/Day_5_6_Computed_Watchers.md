# Day 5-6: Computed Properties & Watchers

## 1. Computed Properties
Computed properties are used to derive state based on other reactive state. They are cached based on their dependencies and only re-evaluate when their dependencies change.

```vue
<script setup>
import { ref, computed } from 'vue'

const author = reactive({
  name: 'John Doe',
  books: [
    'Vue 2 - Advanced Guide',
    'Vue 3 - Basic Guide',
    'Vue 4 - The Mystery'
  ]
})

// A computed ref
const publishedBooksMessage = computed(() => {
  return author.books.length > 0 ? 'Yes' : 'No'
})
</script>

<template>
  <p>Has published books:</p>
  <span>{{ publishedBooksMessage }}</span>
</template>
```

## 2. Watchers
While computed properties are for deriving data, watchers (`watch` and `watchEffect`) are for performing "side effects" in reaction to state changes (like fetching data, mutating the DOM, or saving to local storage).

```vue
<script setup>
import { ref, watch } from 'vue'

const question = ref('')
const answer = ref('Questions usually contain a question mark. ;-)')

// watch works directly on a ref
watch(question, async (newQuestion, oldQuestion) => {
  if (newQuestion.includes('?')) {
    answer.value = 'Thinking...'
    // perform API call here
  }
})
</script>
```

## 3. Class and Style Bindings
You can dynamically bind HTML classes and inline styles using `v-bind:class` (`:class`) and `:style`.

```html
<!-- Object syntax -->
<div :class="{ active: isActive, 'text-danger': hasError }"></div>

<!-- Array syntax -->
<div :class="[activeClass, errorClass]"></div>
```

---

## 🚀 Your Assignment
1. Create a `shoppingList` array of objects (each item having a `name`, `price`, and `purchased` boolean).
2. Create a `computed` property that calculates the total price of all items that are **not** purchased.
3. Add a `:class` binding to strike through (`text-decoration: line-through`) the names of items that are purchased.
