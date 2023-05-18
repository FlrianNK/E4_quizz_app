export default {
  clear() {
    window.localStorage.removeItem("playerName");
    window.localStorage.removeItem("participationScore");
    window.localStorage.removeItem("adminQuestionSelected");
  },
  clearAdminMode() {
    this.clear();
    window.localStorage.removeItem("tokenTime");
    window.localStorage.removeItem("token");
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
  saveToken(token) {
    window.localStorage.setItem("token", token);
    window.localStorage.setItem("tokenTime", new Date().getTime());
  },
  getToken() {
    var storedTime = localStorage.getItem("tokenTime");
    if (storedTime) {
      var currentTime = new Date().getTime();
      if (currentTime - parseInt(storedTime) > 3600000) {
        window.localStorage.removeItem("token");
        window.localStorage.removeItem("tokenTime");
      }
    }
    return window.localStorage.getItem("token");
  },
  saveAdminQuestion(position) {
    window.localStorage.setItem("adminQuestionSelected", String(position));
  },
  getAdminQuestion() {
    return parseInt(window.localStorage.getItem("adminQuestionSelected"));
  },
};
