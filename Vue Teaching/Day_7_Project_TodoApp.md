# Day 7: Weekend Project - Task Tracker

It's time to put everything you've learned in Week 1 together! 

## 🎯 Goal
Build a fully functional Task Tracker (Todo App) inside your `vue-playground` project.

## 📋 Requirements
1. **Add Tasks**: A form with an input field to add new tasks. Use `v-model` to bind the input.
2. **List Tasks**: Use `v-for` to render the list of tasks.
3. **Delete Tasks**: A button next to each task to remove it from the list. Use event handling (`@click`).
4. **Complete Tasks**: A checkbox next to each task to mark it as complete. Use `:class` binding to apply a "completed" styling (e.g., strikethrough text, gray background).
5. **Computed Stats**: Show the total number of tasks, and the number of completed tasks using `computed` properties.

## 💡 Hints
- Use a `ref` for the new task input string.
- Use a `ref` holding an array of objects for the tasks. E.g. `[{ id: 1, text: 'Learn Vue', completed: false }]`.
- For the `id`, you can simply use `Date.now()`.

---

Once you finish this project, you will have successfully mastered Vue fundamentals! Let me know if you run into any bugs or need help structuring the code.
