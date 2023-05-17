<template>
  <div class="QuestionList">
    <h1>QuestionList</h1>
    <ol>
      <li v-for="question in questionList" v-bind:key="question.position">
        <a @click="handleQuestion(question)">{{ question.title }}</a>
      </li>
    </ol>
    <button type="button">Créer une question</button>
  </div>
</template>

<script>
import quizApiService from "@/services/QuizApiService";
export default {
  data() {
    return {
      questionList: [],
    };
  },
  async created() {
    let apiResponse = await quizApiService.getQuizInfo();
    this.setQuestionList(apiResponse.data.size);
  },
  props: {
    question: {
      type: Object,
      required: true,
    },
  },
  emits: ["question-selected", "good-answer"],
  methods: {
    async setQuestionList(questionsTotalNumber) {
      let currentQuestion;
      for (let i = 1; i <= questionsTotalNumber; i++) {
        let currentQuestionResponse = await quizApiService.getQuestion(i);
        currentQuestion = currentQuestionResponse.data;
        this.questionList.push(currentQuestion);
      }
    },
    handleQuestion(question) {
      this.$emit("question-selected", question);
    },
  },
};
</script>
