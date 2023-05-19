<template>
  <div v-if="question != null" class="QuestionDisplay">
    <h2>{{ question.title }}</h2>
    <div class="question-display">
      <div class="question-content">
        <p>{{ question.text }}</p>
        <img v-if="question.image" :src="question.image" alt="Base64 Image" />
      </div>
      <ol type="A" class="answer-list">
        <li
          v-for="(answer, index) in question.possibleAnswers"
          :key="index"
          @click="handleAnswer(index + 1)"
        >
          {{ answer.text }}
        </li>
      </ol>
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

<style scoped>
.QuestionDisplay {
  margin-top: 20px;
  display: flex;
  flex-direction: column;
  justify-content: center;
}

h2 {
  color: #541b5f;
  font-size: 38px;
}

.question-display {
  margin-top: 20px;
  width: 100%;
  border-radius: 25px;
  border: 2px solid #e3d2e2;
  padding: 30px;
}
.question-content {
  padding-bottom: 30px;
  margin: 30px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  text-align: center;
  font-size: 20px;
}

.question-content p {
  border-top: 2px solid #8b269f;
  margin-right: 80px;
  padding-top: 20px;
}

.question-content img {
  width: 300px;
  height: auto;
  border-radius: 15px;
  border: 2px solid #e3d2e2;
}
.answer-list {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  grid-gap: 15px;
}

.answer-list li {
  text-align: center;
  font-size: 16px;
  color: var(--color-text);
  background-color: #ffffff;
  border-radius: 50px;
  border: 2px solid #e3d2e2;
  padding: 5px 50px;
  transition: background-color 0.3s ease;
  list-style-position: inside;
}

.answer-list li:hover {
  color: #e3d2e2;
  background-color: #460b50cb;
}
</style>
