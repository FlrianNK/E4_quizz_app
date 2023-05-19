<script setup>
import { RouterLink, RouterView } from "vue-router";
</script>

<template>
  <header>
    <div class="naviguation-bar">
      <nav>
        <div class="logo">
          <img src="./components/logo.jpg" alt="logo" />
          <p>Jelly Quiz</p>
        </div>
        <div class="links">
          <RouterLink to="/">Home</RouterLink>
          <RouterLink to="/admin">Administration</RouterLink>
        </div>
      </nav>
    </div>
  </header>

  <RouterView />
</template>

<style scoped>
header {
  background-color: #541b5f;
  font-size: 18x;
  color: #c2a1c9;
}

.links {
  float: none;
  position: absolute;
  height: 100%;
  width: 30%;
  display: flex;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}
.links a {
  color: #b164c1;
  text-decoration: none;
  height: inherit;
  width: 50%;
  display: flex;
  justify-content: center;
  align-items: center;
}

.logo {
  display: flex;
  margin-left: 15vw;
  align-items: center;
}
.logo > p {
  font-style: italic;
  font-size: 15px;
  margin-top: 5px;
}
.logo > img {
  width: 35px;
  height: 35px;
  border-radius: 10%;
  margin-right: 10px;
}
nav a.router-link-exact-active {
  color: #e3d2e2;
}
</style>
