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
    quizInfoApiResult = {
      data: {
        scores: [
          {
            date: "18/04/2022 11:57:48",
            playerName: "Emil",
            score: 10,
          },
          {
            date: "18/04/2022 11:57:48",
            playerName: "Dora",
            score: 8,
          },
          {
            date: "18/04/2022 11:57:49",
            playerName: "Gustav",
            score: 7,
          },
        ],
        size: 3,
      },
      status: 200,
    };
    this.registeredScores = quizInfoApiResult.data.scores;
    console.log("Composant Home page 'created'");
    console.log(this.registeredScores);
  },
};
</script>
