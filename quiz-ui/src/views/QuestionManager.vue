<template>
  <div class="QuestionManager">
    <h1>
      Question {{ currentQuestionPosition }} / {{ totalNumberOfQuestions }}
    </h1>
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
    this.loadQuestionByPosition(this.currentQuestionPosition);
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
