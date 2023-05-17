<template>
  <div class="AdminPage">
    <h1>AdminPage</h1>
    <div v-if="!adminMode">
      <input type="password" v-model="password" />
      <button type="button" @click="login">Connexion</button>
      <p v-if="showErrorMessage" class="error-message">Mauvais mot de passe</p>
    </div>
    <div v-if="adminMode">
      <button type="button" @click="disconnect">Déconnexion</button>
      <QuestionsList />
    </div>
  </div>
</template>

<script>
import QuestionsList from "./QuestionsList.vue";
import participationStorageService from "@/services/ParticipationStorageService";
import quizApiService from "@/services/QuizApiService";

export default {
  components: {
    QuestionsList,
  },
  data() {
    return {
      password: "",
      showErrorMessage: false,
      adminMode: false,
      questionSelected: null,
    };
  },
  created() {
    this.adminMode = participationStorageService.getToken();
  },
  methods: {
    async login() {
      let loginResponse = await quizApiService.postLogin(this.password);
      if (loginResponse) {
        this.showErrorMessage = false;
        console.log(loginResponse);
        participationStorageService.saveToken(loginResponse.data.token);
        location.reload();
      } else {
        this.showErrorMessage = true;
      }
    },
    disconnect() {
      participationStorageService.clearAdminMode();
      location.reload();
    },
  },
};
</script>
