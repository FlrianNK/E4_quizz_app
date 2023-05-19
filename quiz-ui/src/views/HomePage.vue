<template>
  <div class="HomePage">
    <img class="logo" src="../components/logo.jpg" alt="logo" />
    <h1>Jelly Quiz</h1>
    <ParticipationDisplay :registeredScores="registeredScores" />
    <router-link class="new-quiz" to="/start-new-quiz-page"
      >Démarrer le quiz !</router-link
    >
  </div>
</template>

<script>
import quizApiService from "@/services/QuizApiService";
import participationStorageService from "@/services/ParticipationStorageService";
import ParticipationDisplay from "./ParticipationDisplay.vue";

export default {
  components: {
    ParticipationDisplay,
  },
  data() {
    return {
      registeredScores: [],
    };
  },
  async created() {
    participationStorageService.clear();
    var quizInfoApiResult = await quizApiService.getQuizInfo();
    this.registeredScores = quizInfoApiResult.data.scores;
  },
};
</script>

<style scoped>
.HomePage {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
  margin-top: 20px;
}
h1 {
  margin-top: 20px;
}
.logo {
  width: 150px;
  height: 150px;
  border-radius: 10%;
}
a.new-quiz {
  display: inline-block;
  text-decoration: none;
  color: var(--color-text);
  background-color: #ffffff;
  border-radius: 50px;
  border: 2px solid #e3d2e2;
  padding: 10px 20px;
  font-size: 18px;
  margin-top: 35px;
  transition: background-color 0.3s ease;
}

a.new-quiz:hover {
  color: #e3d2e2;
  background-color: #460b50cb;
}
</style>
