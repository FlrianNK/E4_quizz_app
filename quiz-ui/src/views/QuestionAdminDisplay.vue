<template>
  <div v-if="currentQuestion != null" class="QuestionAdminDisplay">
    <h1>QuestionAdminDisplay</h1>
    <button type="button" @click="back">Retour</button>
    <button type="button" @click="disconnect">Déconnexion</button>
    <h2>Titre:</h2>
    <p>{{ currentQuestion.title }}</p>
    <h2>Intitulé:</h2>
    <p>{{ currentQuestion.text }}</p>
    <h2>Liste des réponses:</h2>
    <ul>
      <li
        v-for="(answer, index) in currentQuestion.possibleAnswers"
        :key="index"
      >
        <span :class="{ marker: answer.isCorrect }">{{ answer.text }}</span>
      </li>
    </ul>
    <button type="button" @click="editQuestion">Éditer</button>
    <button type="button" @click="deleteQuestion">Supprimer</button>
    <QuestionEdition v-if="edit" :question="currentQuestion" :edit="true" />
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
      currentQuestion: null,
      edit: false,
    };
  },
  async created() {
    let position = participationStorageService.getAdminQuestion();
    let response = await quizApiService.getQuestion(position);
    this.currentQuestion = response.data;
  },
  methods: {
    disconnect() {
      participationStorageService.clearAdminMode();
      this.$router.push("/admin");
    },
    back() {
      this.$router.push("/admin");
    },
    editQuestion() {
      this.edit = !this.edit;
    },
    async deleteQuestion() {
      const token = participationStorageService.getToken();
      await quizApiService.deleteQuestion(this.currentQuestion.id, token);
      this.$router.push("/admin");
    },
  },
};
</script>

<style>
.QuestionAdminDisplay {
  margin-top: 40px;
  margin-right: 15vw;
  margin-left: 15vw;
}
.marker {
  background-color: rgba(61, 146, 61, 0.538);
}
</style>
