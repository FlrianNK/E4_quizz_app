<template>
  <div v-if="currentQuestion != null" class="QuestionManager">
    <h2>
      Question {{ currentQuestionPosition }} / {{ totalNumberOfQuestions }}
    </h2>
    <QuestionDisplay
      :question="currentQuestion"
      @answer-selected="answerClickedHandler"
    />
  </div>
</template>

<script>
import QuestionDisplay from "./QuestionDisplay.vue";
import quizApiService from "@/services/QuizApiService";
import participationStorageService from "@/services/ParticipationStorageService";

export default {
  components: {
    QuestionDisplay,
  },
  data() {
    return {
      currentQuestionPosition: 1,
      totalNumberOfQuestions: 0,
      currentQuestion: null,
      answersList: [],
    };
  },
  async created() {
    var quizInfoApiResult = await quizApiService.getQuizInfo();
    this.totalNumberOfQuestions = quizInfoApiResult.data.size;
    if (this.totalNumberOfQuestions == 0) {
      this.$router.push("/");
    } else {
      this.loadQuestionByPosition(this.currentQuestionPosition);
    }
  },
  methods: {
    async loadQuestionByPosition(position) {
      let result = await quizApiService.getQuestion(position);
      this.currentQuestion = result.data;
    },
    async answerClickedHandler(answer) {
      this.answersList.push(answer);
      if (this.currentQuestionPosition < this.totalNumberOfQuestions) {
        this.currentQuestionPosition++;
        this.loadQuestionByPosition(this.currentQuestionPosition);
      } else {
        this.endQuiz();
      }
    },
    async endQuiz() {
      console.log(this.answersList);
      let postParticipation = await quizApiService.postParticipation({
        playerName: participationStorageService.getPlayerName(),
        answers: this.answersList,
      });
      participationStorageService.saveParticipationScore(
        postParticipation.data.score
      );
      this.$router.push("/scores");
    },
  },
};
</script>

<style scoped>
.QuestionManager {
  margin-top: 40px;
  margin-right: 15vw;
  margin-left: 15vw;
}
h2 {
  width: fit-content;
  color: white;
  background-color: #732183df;
  border-radius: 50px;
  border: 2px solid #e3d2e2;
  padding: 10px 20px;
}
</style>
