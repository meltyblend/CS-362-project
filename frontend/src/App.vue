<!--This is where I will be doing the Frontend of the project
use "npm run dev" to see the changes-->


<script setup lang="ts">
// importing vue and vue router elements
import { RouterLink, RouterView } from 'vue-router'
import { onMounted, nextTick } from 'vue'

// lifecycle hook triggered once when the component is mounted to the DOM
onMounted(() => {
  // waits for vue to update DOM before executing MathJaX
  nextTick().then(() => {
    if ((window as any).MathJax) { // checking if mathjax is loaded and available globally
      window.MathJax.typesetPromise();  // explicitly renders mathjax/math content
    }
  });
});
</script>

<template>
  <div>
    When \( a \ne 0 \), there are two solutions to \( ax^2 + bx + c = 0 \):
    \[
      x = {-b \pm \sqrt{b^2 - 4ac} \over 2a}
    \]
  </div>
</template>

<style scoped>
header {
  line-height: 1.5;
  max-height: 100vh;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}

nav {
  width: 100%;
  font-size: 12px;
  text-align: center;
  margin-top: 2rem;
}

nav a.router-link-exact-active {
  color: var(--color-text);
}

nav a.router-link-exact-active:hover {
  background-color: transparent;
}

nav a {
  display: inline-block;
  padding: 0 1rem;
  border-left: 1px solid var(--color-border);
}

nav a:first-of-type {
  border: 0;
}

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }

  nav {
    text-align: left;
    margin-left: -1rem;
    font-size: 1rem;

    padding: 1rem 0;
    margin-top: 1rem;
  }
}
</style>
