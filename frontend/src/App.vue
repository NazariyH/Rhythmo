<template>
  <Navbar />
  <router-view />
</template>


<script>
import Navbar from '@/components/Navbar.vue'
import axios from 'axios'

export default {
  components: {
    Navbar,
  },
  beforeCreate() {
    this.$store.commit('initializeStore')

    const token = this.$store.state.token

    if (token) {
      axios.defaults.headers.common['Authorization'] = 'Token ' + token
    } else {
      axios.defaults.headers.common['Authorization'] = ''
    }
  },
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
body,
h1,
h2,
h3,
h4,
h5,
h6,
p,
ul,
ol,
li,
button,
input,
textarea,
select {
  margin: 0;
  padding: 0;
}

/* Remove list styles */
ul,
ol {
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
  background-color: #fcf4ea;

  overflow-x: hidden;
}

/* Ensure all elements inherit font color */
body,
h1,
h2,
h3,
h4,
h5,
h6,
p,
ul,
ol,
li,
a,
button,
textarea,
select {
  color: inherit;
}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;

  a {
    font-weight: bold;
    color: #000000;

    &.router-link-exact-active {
      color: #9b9b9b !important;
    }
  }

  .navbar-menu ul li a.router-link-exact-active::before,
  .verical-navbar-menu ul li a.router-link-exact-active::before {
    background-color: #9b9b9b !important;
  }
}

.section {
  min-height: 100vh;

  form {
    width: 720px !important;
    padding: 0 20px;
  }
}

@media(max-width: 800px) {
  .section {
    form {
      width: auto !important;
    }
  }
}
</style>
