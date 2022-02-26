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
    name: "Courses",
    component: () => import("@/pages/courses/CoursePage.vue"),
    meta: {
      title: "My Courses"
    }
  },
  {
    path: "/about",
    name: "About",
    component: () => import("@/pages/more/About.vue"),
    meta: {
      title: "About Us"
    }
  },
  {
    path: "/faq",
    name: "FAQ",
    component: () => import("@/pages/more/Faq.vue"),
    meta: {
      title: "FAQs"
    }
  }
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
