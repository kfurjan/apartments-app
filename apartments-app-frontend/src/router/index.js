import Vue from "vue";
import VueRouter from "vue-router";
import store from "../store/index.js"

import Home from "../views/Home.vue";
import Login from "../views/Login.vue";
import Settings from "../views/Settings.vue";
import Register from "../views/Register.vue";
import Restricted from "../views/Restricted.vue";
import ApartmentDetails from "../views/ApartmentDetails.vue";
import Apartments from "../views/renter/Apartments.vue";
import Reservations from "../views/Reservations.vue";
import ApartmentForm from "../views/renter/ApartmentForm.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/login",
    name: "Login",
    component: Login,
  },
  {
    path: "/settings",
    name: "Settings",
    component: Settings,
    meta: {
      requiresAuth: true
    },
  },
  {
    path: "/register",
    name: "Register",
    component: Register,
  },
  {
    path: "/restricted",
    name: "Restricted",
    component: Restricted,
    meta: {
      requiresAuth: true
    },
  },
  {
    path: "/apartment/:id",
    name: "Apartment",
    component: ApartmentDetails,
  },
  {
    path: "/renter/apartments",
    name: "Apartments",
    component: Apartments,
    meta: {
      requiresAuth: true
    },
  },
  {
    path: "/renter/apartments/new",
    name: "ApartmentForm",
    component: ApartmentForm,
    props: { mode: 'Create' },
    meta: {
      requiresAuth: true
    },
  },
  {
    path: "/renter/apartments/:id/edit",
    name: "ApartmentForm",
    component: ApartmentForm,
    props: { mode: 'Update' },
    meta: {
      requiresAuth: true
    },
  },
  {
    path: "/reservations",
    name: "Reservations",
    component: Reservations,
    meta: {
      requiresAuth: true
    },
  }
];

const router = new VueRouter({
  routes,
});

router.beforeEach((to, from, next) => {
  store.dispatch('loadCurrentUser')
  const user = store.getters.currentUser

  if (user) {

    if (to.name == 'Settings' || user.roleId) {
      return next() // go to wherever I'm going
    }
    else {
      return next({ name: 'Settings' })
    }
  }


  if (to.matched.some(record => record.meta.requiresAuth)) {
    // this route requires auth, check if logged in
    // if not, redirect to login page.
    if (user) {
      return next()
    } else {
      return next({ name: 'Login' })
    }
  } else {
    return next() // does not require auth, make sure to always call next()!
  }
})

export default router;
