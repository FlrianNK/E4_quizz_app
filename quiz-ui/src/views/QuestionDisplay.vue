<template>
  <div v-if="question != null" class="QuestionDisplay">
    <h2>{{ question.title }}</h2>
    <img v-if="question.image" :src="question.image" alt="Base64 Image" />
    <p>{{ question.text }}</p>
    <div v-for="(answer, index) in question.possibleAnswers" :key="index">
      <a @click="handleAnswer(index + 1)">{{ answer.text }}</a>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    question: {
      type: Object,
      required: true,
    },
  },
  emits: ["answer-selected"],
  methods: {
    handleAnswer(answer) {
      this.$emit("answer-selected", answer);
    },
  },
};
</script>
