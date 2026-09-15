# Day 21: Weekend Project - E-commerce Dashboard

Welcome to the end of Week 3! It's time to build a robust SPA using Vue Router and Pinia.

## 🎯 Goal
Build a mock E-commerce Product Dashboard where users can view products, log in, and add items to a shopping cart.

## 📋 Requirements

### 1. Routing Setup
Create the following routes:
- `/` (Home View) - A simple landing page.
- `/login` (Login View) - A fake login form.
- `/products` (Products View) - A grid of products.
- `/cart` (Cart View) - The user's shopping cart.

### 2. State Management (Pinia)
Create two stores:
- **`authStore`**: Manages `isLoggedIn` and the current `user` object.
- **`cartStore`**: Manages an array of `items` in the cart. It should have an action `addToCart(product)` and a getter `totalPrice`.

### 3. Navigation Guards
- Protect the `/cart` route. If a user is not logged in, redirect them to `/login`.
- If the user is on the `/login` route and successfully logs in, redirect them back to the page they were trying to access (or `/products`).

## 💡 Hints
- Mock your product data using a static array of objects in your component or a separate `data.js` file (e.g., `[ { id: 1, name: 'Laptop', price: 999 }, ... ]`).
- In your App header, display a small shopping cart icon with a badge showing the `cartStore.items.length`.

Good luck! This project simulates the core architecture of almost every modern web application.
