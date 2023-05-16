<template>
  <div class="AdminPage">
    <h1>AdminPage</h1>
    <div v-if="!isTokenValid()">
      <input type="password" v-model="password" />
      <button type="button" @click="login">Connexion</button>
      <p v-if="showErrorMessage" class="error-message">Mauvais mot de passe</p>
    </div>
    <div v-if="isTokenValid()">
      <QuestionsList />
      <QuestionEdition />
      <QuestionAdminDisplay />
    </div>
  </div>
</template>

<script>
import QuestionsList from "./QuestionsList.vue";
import QuestionEdition from "./QuestionEdition.vue";
import QuestionAdminDisplay from "./QuestionAdminDisplay.vue";
import participationStorageService from "@/services/ParticipationStorageService";
import quizApiService from "@/services/QuizApiService";

export default {
  components: {
    QuestionsList,
    QuestionEdition,
    QuestionAdminDisplay,
  },
  data() {
    return {
      password: "",
      showErrorMessage: false,
    };
  },
  methods: {
    isTokenValid() {
      return participationStorageService.getToken();
    },
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
  },
};
</script>
