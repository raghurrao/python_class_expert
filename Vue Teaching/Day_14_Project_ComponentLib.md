# Day 14: Weekend Project - Component Library

Congratulations on completing Week 2! You now know how to architect robust Vue components.

## 🎯 Goal
Build a mini UI Component Library using Props, Emits, and Slots.

## 📋 Requirements
Create a new folder in `src/components` called `ui`. Inside it, build the following reusable components:

1. **`MyButton.vue`**
   - Accept a `variant` prop (`primary`, `secondary`, `danger`) to change its colors.
   - Use a `<slot>` so the user can pass text or icons inside the button.
   - Forward click events to the parent.

2. **`MyModal.vue`**
   - Accept an `isOpen` boolean prop.
   - Emit a `close` event when the background overlay or an 'X' button is clicked.
   - Use named slots for `#header`, `#body`, and `#footer`.

3. **`MyAccordion.vue`**
   - Accept an array of objects `[{ title: '...', content: '...' }]` as a prop.
   - Allow only one item to be expanded at a time (manage this state internally).

## 💡 Hints
- Test your components by importing them into `App.vue` and using them in different ways.
- For the Modal overlay, you can use absolute positioning and a semi-transparent black background. Use `v-if="isOpen"` on the modal wrapper.

Have fun building this! This is a very common task in real-world frontend development.
