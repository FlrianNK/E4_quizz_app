<template>
  <div class="QuestionAdminDisplay">
    <h1>QuestionAdminDisplay</h1>
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
    <button type="button">Éditer</button>
    <button type="button">Supprimer</button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      selectedOptionIndex: null,
    };
  },
  props: {
    question: {
      type: Object,
      required: true,
    },
  },
  methods: {
    setGoodAnswerIndex() {},
  },
};
</script>

<style>
.marker {
  background-color: rgba(61, 146, 61, 0.538);
}
</style>
