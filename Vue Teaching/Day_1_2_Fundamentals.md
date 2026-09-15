# Day 1-2: Vue 3 Fundamentals & Template Syntax

Welcome to your first lesson! Today, we will cover the basics of Vue 3 and get your development environment set up.

## 1. What is Vue 3?
Vue (pronounced like "view") is a progressive JavaScript framework for building user interfaces. It builds on top of standard HTML, CSS, and JavaScript, and provides a declarative and component-based programming model.

Vue 3 introduces the **Composition API**, a new way to write logic in Vue components that makes it easier to organize and reuse code compared to the older Options API (used in Vue 2).

## 2. Setting Up Your Playground
We'll use **Vite**, a blazing fast build tool, to scaffold our Vue project. I have initialized a project called `vue-playground` for you in this directory.

To run the development server, you will normally run:
```bash
cd vue-playground
npm install
npm run dev
```

## 3. Template Syntax Basics
Vue uses an HTML-based template syntax. Here are the core features:

### Text Interpolation
The most basic form of data binding is text interpolation using the "Mustache" syntax (double curly braces):
```html
<span>Message: {{ msg }}</span>
```

### Attribute Bindings (`v-bind`)
Mustaches cannot be used inside HTML attributes. Instead, use the `v-bind` directive (or its shorthand `:`):
```html
<!-- Full syntax -->
<div v-bind:id="dynamicId"></div>

<!-- Shorthand -->
<div :id="dynamicId"></div>
```

### Conditional Rendering (`v-if`)
You can conditionally render blocks using `v-if`, `v-else-if`, and `v-else`:
```html
<h1 v-if="awesome">Vue is awesome!</h1>
<h1 v-else>Oh no 😢</h1>
```

### List Rendering (`v-for`)
Use the `v-for` directive to render a list of items based on an array:
```html
<ul>
  <li v-for="item in items" :key="item.id">
    {{ item.text }}
  </li>
</ul>
```
*(Always provide a unique `:key` attribute with `v-for` to help Vue track element identity.)*

---

## 🚀 Your Assignment for Today

1. Open the terminal and start the Vite dev server inside the `vue-playground` folder.
2. Open `src/App.vue`.
3. Try defining some static variables in the `<script setup>` tag (e.g., a string `title`, a boolean `isVisible`, and an array of objects `shoppingList`).
4. Use `{{ title }}`, `v-if="isVisible"`, and `v-for` in the `<template>` section to render these variables on the screen.

Let me know once you have completed this, or if you encounter any errors! I can run the setup commands for you right now if you prefer.
