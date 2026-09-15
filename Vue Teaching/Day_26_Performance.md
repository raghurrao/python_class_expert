# Day 26: Performance Optimization in Vue

As you build larger apps, you need to ensure they run smoothly. Here are key performance optimization techniques in Vue 3.

## 1. `v-show` vs `v-if`
- `v-if` actually destroys and recreates the DOM elements when it toggles.
- `v-show` just toggles the CSS `display` property (`display: none`).

**Rule of thumb:** If an element toggles very frequently, use `v-show`. If the condition rarely changes, use `v-if`.

## 2. Using `v-once` and `v-memo`
If a section of your template contains static data that never changes after the first render, you can use `v-once`. Vue will skip checking this element for updates.

```html
<span v-once>This will never change: {{ msg }}</span>
```

`v-memo` is for skipping updates in large lists if specific dependencies haven't changed.

## 3. Shallow Reactivity
Sometimes you have a massive array of objects (e.g., 10,000 rows of data from an API), but you only intend to display them, never mutate their individual properties.
Using `ref` or `reactive` will add overhead because Vue has to deeply proxy every nested property.

Instead, use `shallowRef`:
```javascript
import { shallowRef } from 'vue'

// Vue will only track changes to bigData.value, not mutations inside the array itself.
const bigData = shallowRef([]) 

fetchData().then(res => bigData.value = res)
```

## 4. Keying in `v-for`
Always use a unique `:key` string or number (not an array index) in `v-for`. This helps Vue's Virtual DOM diffing algorithm pinpoint exactly which DOM nodes were moved, added, or removed, rather than re-rendering the whole list.

---

## 🚀 Your Assignment
1. Review your code in the `vue-playground` (specifically the Todo App or Dashboard).
2. Look for places where you can swap `v-if` for `v-show`.
3. Ensure all your `v-for` loops have proper `:key` bindings.
