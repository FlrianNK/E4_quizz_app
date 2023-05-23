<template>
  <div class="QuestionList">
    <h1>QuestionList</h1>
    <ol>
      <li v-for="question in questionList" v-bind:key="question.position">
        <a @click="handleQuestion(question.position)">{{ question.title }}</a>
      </li>
    </ol>
    <button type="button" @click="editQuestion">Créer une question</button>
    <QuestionEdition
      v-if="edit"
      :question="dummyQuestion"
      :edit="false"
      :cancel="cancel"
    />
  </div>
</template>

<script>
import QuestionEdition from "./QuestionEdition.vue";
import quizApiService from "@/services/QuizApiService";
import participationStorageService from "../services/ParticipationStorageService";

export default {
  components: {
    QuestionEdition,
  },
  data() {
    return {
      questionList: [],
      edit: false,
      dummyQuestion: {
        text: "text",
        title: "title",
        image: "falseb64imagecontent",
        position: 1,
        possibleAnswers: [
          {
            text: "reponse 1",
            isCorrect: true,
          },
          {
            text: "reponse 2",
            isCorrect: false,
          },
          {
            text: "reponse 3",
            isCorrect: false,
          },
          {
            text: "reponse 4",
            isCorrect: false,
          },
        ],
      },
    };
  },
  async created() {
    participationStorageService.clear();
    let apiResponse = await quizApiService.getAllQuestion();
    this.questionList = apiResponse.data;
  },
  methods: {
    handleQuestion(position) {
      this.$router.push("/admin/edit");
      participationStorageService.saveAdminQuestion(position);
    },
    editQuestion() {
      this.edit = !this.edit;
    },
    cancel() {
      this.edit = false;
    },
  },
};
</script>
