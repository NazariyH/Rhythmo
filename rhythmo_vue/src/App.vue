<template>
  <Navbar />
  <router-view/>
</template>

<script>
import Navbar from './components/Navbar.vue'

export default {
  components: {
    Navbar,
  }
}
</script>

<style lang="scss">
/* Reset box-sizing */
*,
*::before,
*::after {
    box-sizing: border-box;
}

/* Reset margin and padding */
body, h1, h2, h3, h4, h5, h6, p, ul, ol, li, button, input, textarea, select {
    margin: 0;
    padding: 0;
}

/* Remove list styles */
ul, ol {
    list-style: none;
}

/* Remove link underlines */
a {
    text-decoration: none;
    color: inherit;
}

/* Reset button styles */
button {
    border: none;
    background: none;
    padding: 0;
    font: inherit;
    cursor: pointer;
}

/* Remove default button border and background */
button:focus {
    outline: none;
}

/* Reset input styles */
input,
textarea,
select {
    border: none;
    padding: 0;
    font: inherit;
    color: inherit;
    outline: none;
    box-shadow: none;
}

/* Reset font family */
body {
    font-family: Arial, sans-serif;
}

/* Ensure all elements inherit font color */
body, h1, h2, h3, h4, h5, h6, p, ul, ol, li, a, button, textarea, select {
    color: inherit;
}

</style>
