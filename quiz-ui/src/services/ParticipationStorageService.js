export default {
  clear() {
    window.localStorage.clear();
  },
  savePlayerName(playerName) {
    window.localStorage.setItem("playerName", playerName);
  },
  getPlayerName() {
    return window.localStorage.getItem("playerName");
  },
  saveParticipationScore(participationScore) {
    window.localStorage.setItem(
      "participationScore",
      String(participationScore)
    );
  },
  getParticipationScore() {
    return parseInt(window.localStorage.getItem("participationScore"));
  },
};
