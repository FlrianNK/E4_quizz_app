<template>
  <div class="ScoreDisplay">
    <h1>Your score</h1>
    <p>{{ playerName }}</p>
    <p>{{ result }} / {{ totalNumberOfQuestions }}</p>
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
      playerName: "",
      result: 0,
      totalNumberOfQuestions: 0,
      registeredScores: [],
    };
  },
  async created() {
    var quizInfoApiResult = await quizApiService.getQuizInfo();
    this.playerName = participationStorageService.getPlayerName();
    this.result = participationStorageService.getParticipationScore();
    this.totalNumberOfQuestions = quizInfoApiResult.data.size;
    this.registeredScores = quizInfoApiResult.data.scores;
  },
};
</script>
