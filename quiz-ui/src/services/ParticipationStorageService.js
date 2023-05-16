export default {
  clear() {
    window.localStorage.removeItem("playerName");
    window.localStorage.removeItem("participationScore");
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
        localStorage.removeItem("token");
        localStorage.removeItem("tokenTime");
      }
    }
    return window.localStorage.getItem("token");
  },
};
