<template>
  <h1>Home page</h1>
  <div v-for="scoreEntry in registeredScores" v-bind:key="scoreEntry.date">
    {{ scoreEntry.playerName }} - {{ scoreEntry.score }}
  </div>
  <router-link to="/start-new-quiz-page">Démarrer le quiz !</router-link>
</template>

<script>
import quizApiService from "@/services/QuizApiService";

export default {
  name: "HomePage",
  data() {
    return {
      registeredScores: [],
    };
  },
  async created() {
    var quizInfoApiResult = await quizApiService.getQuizInfo();
    console.log(quizInfoApiResult);
    this.registeredScores = quizInfoApiResult.data.scores;
    console.log("Composant Home page 'created'");
    console.log(this.registeredScores);
  },
};
</script>
