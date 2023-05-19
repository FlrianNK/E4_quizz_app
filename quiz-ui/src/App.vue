<script setup>
import { RouterLink, RouterView } from "vue-router";
</script>

<template>
  <header>
    <div class="wrapper">
      <nav>
        <img class="logo" src="./components/logo.jpg" alt="logo" />
        <p class="nav">Jelly Quiz</p>
        <RouterLink class="nav-link" to="/">Home</RouterLink>
        <RouterLink class="nav-link" to="/admin">Administration</RouterLink>
      </nav>
    </div>
  </header>

  <RouterView />
</template>

<style scoped>
header {
  background-color: #541b5f;
}

nav {
  display: flex;
  justify-content: center;
  align-items: center;
  font-size: 20px;
  width: 100%;
  color: #c2a1c9;
  padding-right: 200px;
}

nav > p {
  margin-right: 80px;
}

.logo {
  justify-content: center;
  align-items: center;
  display: flex;
  font-size: 20px;
}
.logo {
  width: 40px;
  height: 40px;
  border-radius: 10%;
  margin-right: 10px;
}
nav a.nav-link {
  color: #b164c1;
}

nav a.router-link-exact-active {
  color: #e3d2e2;
}

nav a.router-link-exact-active:hover {
  background-color: transparent;
}
</style>
