<template>
  <div class="NewQuizPage">
    <p>Saisissez votre nom :</p>
    <input type="text" v-model="username" />
    <button type="button" @click="launchNewQuiz">GO !</button>
  </div>
</template>

<script>
import participationStorageService from "@/services/ParticipationStorageService";

export default {
  data() {
    return {
      username: "",
    };
  },
  methods: {
    launchNewQuiz() {
      participationStorageService.savePlayerName(this.username);
      this.$router.push("/questions");
    },
  },
};
</script>

<style>
/* @media (min-width: 1024px) {
  .NewQuizPage {
    min-height: 100vh;
    display: flex;
    align-items: center;
  }
} */
</style>
