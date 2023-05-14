<template>
  <div class="ScoreDisplay">
    <h1>Your score</h1>
    <h2>Information</h2>
    <p>Name: {{ playerName }}</p>
    <p>Score: {{ result }} / {{ totalNumberOfQuestions }}</p>
    <h2>Ranking</h2>
    <p>{{ rank }} / {{ registeredScores.length }}</p>
    <h2>All participations</h2>
    <div v-for="scoreEntry in registeredScores" v-bind:key="scoreEntry.date">
      {{ scoreEntry.playerName }} - {{ scoreEntry.score }}
    </div>
  </div>
</template>

<script>
import quizApiService from "@/services/QuizApiService";
import participationStorageService from "@/services/ParticipationStorageService";

export default {
  data() {
    return {
      registeredScores: [],
      playerName: "",
      result: 0,
      rank: 0,
      totalNumberOfQuestions: 0,
    };
  },
  async created() {
    var quizInfoApiResult = await quizApiService.getQuizInfo();
    this.registeredScores = quizInfoApiResult.data.scores;
    this.playerName = participationStorageService.getPlayerName();
    this.result = participationStorageService.getParticipationScore();
    this.rank = this.getRank(
      this.registeredScores,
      this.playerName,
      this.result
    );
    this.totalNumberOfQuestions = quizInfoApiResult.data.size;
  },
  methods: {
    getRank(registeredScores, name, score) {
      const searchCriteria = {
        playerName: name,
        score: score,
      };
      const index = registeredScores.findIndex((obj) => {
        for (let key in searchCriteria) {
          if (obj[key] !== searchCriteria[key]) {
            return false;
          }
        }
        return true;
      });
      return index + 1;
    },
  },
};
</script>
