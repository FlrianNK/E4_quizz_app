<template>
  <div class="NewQuizPage">
    <p>Saisissez votre nom :</p>
    <input type="text" v-model="username" />
    <p v-if="showErrorMessage">Rentrez un nom valide !</p>
    <button class="start-quiz" type="button" @click="launchNewQuiz">
      GO !
    </button>
  </div>
</template>

<script>
import participationStorageService from "@/services/ParticipationStorageService";

export default {
  data() {
    return {
      username: "",
      showErrorMessage: false,
    };
  },
  methods: {
    launchNewQuiz() {
      if(this.username){
        this.showErrorMessage = false;
        participationStorageService.savePlayerName(this.username);
        this.$router.push("/questions");
      }
      else{
        this.showErrorMessage = true;
      }
    },
  },
};
</script>

<style scoped>
.NewQuizPage {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 35vh;
}

.NewQuizPage p,
.NewQuizPage input,
.NewQuizPage button {
  margin-bottom: 25px;
}
.NewQuizPage p {
  font-size: 20px;
}
.NewQuizPage input {
  width: 400px;
}
.start-quiz {
  display: inline-block;
  text-decoration: none;
  color: var(--color-text);
  background-color: #ffffff;
  border-radius: 50px;
  border: 2px solid #e3d2e2;
  padding: 10px 20px;
  font-size: 18px;
  transition: background-color 0.3s ease;
}

.start-quiz:hover {
  color: #e3d2e2;
  background-color: #460b50cb;
}
</style>
