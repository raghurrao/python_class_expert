# Day 8-9: Components, Props, and Custom Events

Welcome to Week 2! We are now diving into Component Architecture.

## 1. What is a Component?
Components allow us to split the UI into independent, reusable pieces. In Vue, components are typically written in Single-File Components (SFCs) with the `.vue` extension.

To use a component, you import it and use it as an HTML tag:
```vue
<!-- Parent.vue -->
<script setup>
import ChildComponent from './ChildComponent.vue'
</script>

<template>
  <ChildComponent />
</template>
```

## 2. Passing Data with Props
Props are custom attributes you can register on a component. They allow you to pass data from a parent to a child.

```vue
<!-- ChildComponent.vue -->
<script setup>
const props = defineProps({
  title: String,
  likes: Number
})
</script>

<template>
  <h3>{{ title }}</h3>
  <p>Likes: {{ likes }}</p>
</template>
```

In the parent:
```vue
<ChildComponent title="My Journey with Vue" :likes="42" />
```

## 3. Emitting Events to the Parent
Since props are one-way (parent to child), children communicate back to parents by emitting custom events using `defineEmits`.

```vue
<!-- ChildComponent.vue -->
<script setup>
const emit = defineEmits(['enlarge-text'])
</script>

<template>
  <button @click="emit('enlarge-text')">Enlarge Text</button>
</template>
```

In the parent, you listen to this custom event just like a normal DOM event:
```vue
<ChildComponent @enlarge-text="postFontSize += 0.1" />
```

---

## 🚀 Your Assignment
1. Refactor your Day 7 Todo App by extracting the individual Task item into its own `TaskItem.vue` component.
2. Pass the task object to `TaskItem.vue` as a Prop.
3. Emit a `delete` and `toggle` event from the `TaskItem.vue` back to the parent `App.vue` to modify the global task list.
