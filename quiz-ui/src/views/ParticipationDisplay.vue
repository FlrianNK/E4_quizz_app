<template>
  <div v-if="registeredScores.length > 0" class="score-entry">
    <div class="score-header">
      <span class="score-header">Nom</span>
      <span class="score-header">Score</span>
    </div>
    <div
      v-for="scoreEntry in registeredScores"
      :key="scoreEntry.date"
      class="score-item"
    >
      <span class="player-name">{{ scoreEntry.playerName }}</span>
      <span class="score">{{ scoreEntry.score }}</span>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    registeredScores: {
      type: Array,
      required: true,
    },
  },
};
</script>

<style scoped>
.score-entry {
  width: 300px;
  padding-top: 15px;
  border-top: 2px solid #8b269f;
  margin-top: 35px;
}

.score-header {
  display: flex;
  justify-content: space-between;
  font-size: 18px;
  font-weight: bold;
  margin-bottom: 5px;
}

.score-item {
  display: flex;
  justify-content: space-between;
  font-size: 16px;
  margin-bottom: 5px;
}
</style>
