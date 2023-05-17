<template>
  <div v-if="question != null" class="QuestionAdminDisplay">
    <h1>QuestionAdminDisplay</h1>
    <button type="button" @click="back">Retour</button>
    <button type="button" @click="disconnect">Déconnexion</button>
    <h2>Titre:</h2>
    <p>{{ question.title }}</p>
    <h2>Intitulé:</h2>
    <p>{{ question.text }}</p>
    <h2>Liste des réponses:</h2>
    <ul>
      <li v-for="(answer, index) in question.possibleAnswers" :key="index">
        <span :class="{ marker: answer.isCorrect }">{{ answer.text }}</span>
      </li>
    </ul>
    <button type="button" @click="editQuestion">Éditer</button>
    <button type="button">Supprimer</button>
    <QuestionEdition v-if="edit" />
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
      question: null,
      edit: false,
    };
  },
  async created() {
    let position = participationStorageService.getAdminQuestion();
    let response = await quizApiService.getQuestion(position);
    this.question = response.data;
  },
  methods: {
    disconnect() {
      participationStorageService.clearAdminMode();
      location.reload();
    },
    back() {
      this.$router.push("/admin");
    },
    editQuestion() {
      this.edit = !this.edit;
    },
  },
};
</script>

<style>
.marker {
  background-color: rgba(61, 146, 61, 0.538);
}
</style>
