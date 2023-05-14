<template>
  <div class="AdminPage">
    <h1>AdminPage</h1>
    <h2>Token not valid</h2>
    <input type="password" v-model="password" />
    <button type="button" @click="login">Connexion</button>
    <h2>Token valid</h2>
    <QuestionsList />
    <QuestionEdition />
    <QuestionAdminDisplay />
  </div>
</template>

<script>
import QuestionsList from "./QuestionsList.vue";
import QuestionEdition from "./QuestionEdition.vue";
import QuestionAdminDisplay from "./QuestionAdminDisplay.vue";

export default {
  components: {
    QuestionsList,
    QuestionEdition,
    QuestionAdminDisplay,
  },
  data() {
    return {
      password: "",
    };
  },
  methods: {
    login() {
      console.log(this.password);
    },
  },
};
</script>
