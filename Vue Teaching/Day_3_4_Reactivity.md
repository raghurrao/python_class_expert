# Day 3-4: Reactivity Fundamentals & Event Handling

## 1. Deep Dive into Reactivity: `ref` vs `reactive`
In Vue 3, reactivity is powered by JavaScript Proxies. You have two main ways to declare reactive state:

### `ref` (For primitive types)
`ref` takes a primitive value (like a string, number, or boolean) and wraps it in a reactive object under the `.value` property.
```vue
<script setup>
import { ref } from 'vue'

const count = ref(0)
console.log(count.value) // 0

// To mutate:
function increment() {
  count.value++
}
</script>

<template>
  <!-- In the template, Vue automatically unwraps the ref, so you omit .value -->
  <button @click="increment">{{ count }}</button>
</template>
```

### `reactive` (For objects and arrays)
`reactive` makes an entire object deeply reactive. You don't need `.value`.
```vue
<script setup>
import { reactive } from 'vue'

const state = reactive({
  user: 'Alice',
  age: 25
})

function birthday() {
  state.age++
}
</script>
```

## 2. Event Handling (`v-on` or `@`)
To listen to DOM events, use the `v-on` directive, or the shorthand `@`.
```html
<!-- Inline handler -->
<button @click="count++">Add 1</button>

<!-- Method handler -->
<button @click="increment">Add 1</button>
```

## 3. Two-Way Data Binding (`v-model`)
For form inputs, Vue provides `v-model` to sync the input value with your state automatically.
```html
<input v-model="text" placeholder="Type here">
<p>You typed: {{ text }}</p>
```

---

## 🚀 Your Assignment
1. Create a simple counter with an "Increment" and "Decrement" button.
2. Create a form with an input for a user's name and age, using `v-model` and a `reactive` object.
3. Display the name and age dynamically on the screen as the user types.
