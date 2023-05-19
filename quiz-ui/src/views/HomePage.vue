<template>
  <div class="HomePage">
    <img class="logo" src="../components/logo.jpg" alt="logo" />
    <h1>Jelly Quiz</h1>
    <div v-if="registeredScores.length > 0" class="score-entry">
      <div class="score-header">
        <span class="score-header">Nom</span>
        <span class="score-header">Score</span>
      </div>
      <div
        v-for="scoreEntry in registeredScores"
        :key="scoreEntry.date"
        class="score-item"
      >
        <span class="player-name">{{ scoreEntry.playerName }}</span>
        <span class="score">{{ scoreEntry.score }}</span>
      </div>
    </div>

    <router-link class="new-quiz" to="/start-new-quiz-page"
      >Démarrer le quiz !</router-link
    >
  </div>
</template>

<script>
import quizApiService from "@/services/QuizApiService";
import participationStorageService from "@/services/ParticipationStorageService";

export default {
  name: "HomePage",
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
.score-entry {
  width: 300px;
  padding-top: 15px;
  border-top: 2px solid #8b269f;
  margin-top: 35px;
}

.score-header {
  display: flex;
  justify-content: space-between;
  font-size: 18px;
  font-weight: bold;
  margin-bottom: 5px;
}

.score-item {
  display: flex;
  justify-content: space-between;
  font-size: 16px;
  margin-bottom: 5px;
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
