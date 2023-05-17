import { createRouter, createWebHistory } from "vue-router";
import HomePage from "../views/HomePage.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "HomePage",
      component: HomePage,
    },
    {
      path: "/start-new-quiz-page",
      name: "start-new-quiz-page",
      component: () => import("../views/NewQuizPage.vue"),
    },
    {
      path: "/questions",
      name: "questions",
      component: () => import("../views/QuestionManager.vue"),
    },
    {
      path: "/scores",
      name: "scores",
      component: () => import("../views/ScorePage.vue"),
    },
    {
      path: "/admin",
      name: "admin",
      component: () => import("../views/AdminPage.vue"),
    },
    {
      path: "/admin/edit",
      name: "admin/edit",
      component: () => import("../views/QuestionAdminDisplay.vue"),
    },
  ],
});

export default router;
