<template>
  <link
    rel="stylesheet"
    href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css"
  />
  <div class="ScoreDisplay">
    <div v-if="registeredScores.length > 0">
      <h2>Liste des participations</h2>
      <ParticipationDisplay :registeredScores="registeredScores" />
    </div>
    <div class="right-column">
      <h1>Résultat</h1>
      <div class="top-border">
        <i class="fa-solid fa-circle-info"></i>
        <h2>
          <i class="fa fa-info-circle" aria-hidden="true"></i> Information
        </h2>
        <p>Nom: {{ playerName }}</p>
        <p>Score: {{ result }} / {{ totalNumberOfQuestions }}</p>
      </div>
      <div class="top-border">
        <h2><span class="fa fa-star checked"></span> Ranking</h2>
        <p>{{ rank }} / {{ registeredScores.length }}</p>
      </div>
    </div>
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

<style scoped>
.ScoreDisplay {
  margin-top: 40px;
  margin-right: 15vw;
  margin-left: 15vw;
  display: flex;
  justify-content: center;
}
.right-column {
  margin-left: 10vh;
  height: 50vh;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  text-align: center;
  border-radius: 25px;
  border: 2px solid #e3d2e2;
  padding: 5px 50px;
}

.top-border > p {
  font-size: 18px;
}

.top-border {
  border-top: 2px solid #8b269f;
}

.checked,
.fa-info-circle {
  color: #541b5f;
}
</style>
