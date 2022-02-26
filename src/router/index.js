import { createRouter, createWebHistory } from "vue-router";

const routes = [
  {
    path: "/",
    name: "Home",
    component: () => import("@/pages/Home.vue"),
    meta: {
      title: "Course Connect",
    },
  },
  {
    path: "/courses",
    namae: "Courses",
    compnent: () => import("@/pages/courses/CoursePage.vue"),
    meta: {
      title: "My Courses"
    }
  }
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
