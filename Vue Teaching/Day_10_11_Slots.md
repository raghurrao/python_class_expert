# Day 10-11: Slots

## 1. What are Slots?
While props allow you to pass JavaScript data into a component, **slots** allow you to pass HTML content (or other components) into a component. They are essentially placeholders in a child component that the parent can fill.

```vue
<!-- CustomButton.vue -->
<template>
  <button class="fancy-btn">
    <slot></slot> <!-- Content goes here -->
  </button>
</template>
```

In the parent:
```vue
<CustomButton>
  Click me! 🚀
</CustomButton>
```

## 2. Named Slots
Sometimes you need multiple slots in a single component (e.g., a modal with a header, body, and footer). You can name your slots:

```vue
<!-- ModalLayout.vue -->
<template>
  <div class="modal">
    <header>
      <slot name="header"></slot>
    </header>
    <main>
      <slot></slot> <!-- default slot -->
    </main>
    <footer>
      <slot name="footer"></slot>
    </footer>
  </div>
</template>
```

In the parent:
```vue
<ModalLayout>
  <template #header>
    <h1>Warning</h1>
  </template>

  <p>Are you sure you want to delete this?</p> <!-- Default slot content -->

  <template #footer>
    <button>Cancel</button>
    <button>Confirm</button>
  </template>
</ModalLayout>
```

## 3. Scoped Slots (Advanced)
Scoped slots allow the child component to pass data back *up* to the slot content in the parent. This is highly useful for creating list components where the child manages the loop, but the parent defines how each item looks.

---

## 🚀 Your Assignment
1. Create a `Card.vue` component that accepts a `header`, a default `body`, and a `footer` slot.
2. Use this Card component in your `App.vue` multiple times with different content.
