<template>
  <v-app>
    <v-app-bar app color="primary" dark>
      <div class="d-flex align-center mr-3">
        <v-app-bar-nav-icon
          @click="toggleDrawer"
          v-if="isLoggedIn"
        ></v-app-bar-nav-icon>
        <v-img
          alt="Vuetify Logo"
          class="shrink mr-2"
          contain
          src="https://cdn.vuetifyjs.com/images/logos/vuetify-logo-dark.png"
          transition="scale-transition"
          width="40"
        />
        <v-toolbar-title style="cursor: pointer" @click="$router.push('/')"
          >ApartmentsApp</v-toolbar-title
        >
      </div>

      <!-- <div>
        <div v-if="isLoggedIn">
          <v-icon color="green" class="mr-2">mdi-checkbox-marked-circle</v-icon>
          <span> Logged in! </span>
        </div>
        <div v-else>
          <v-icon color="red darken-2" class="mr-2">mdi-cancel</v-icon>
          <span> Not logged in </span>
        </div>
      </div> -->

      <v-spacer></v-spacer>

      <template v-if="!isLoggedIn">
        <v-btn to="/login" text height="100%">Login</v-btn>
        <v-divider vertical></v-divider>
        <v-btn to="/register" text height="100%">Register</v-btn>
      </template>
      <!-- <v-btn color="error" to="/restricted">Restricted</v-btn> -->
    </v-app-bar>

    <navigation></navigation>

    <v-main>
      <router-view />
    </v-main>

    <!-- <v-snackbar v-model="snackbarShow" timeout="2000">
      {{ snackbarText }}

      <template v-slot:action="{ attrs }">
        <v-btn color="pink" text v-bind="attrs" @click="snackbarShow = false">
          Close
        </v-btn>
      </template>
    </v-snackbar> -->
  </v-app>
</template>

<script>
import Navigation from "./components/Navigation.vue";
export default {
  name: "App",
  components: {
    Navigation,
  },
  computed: {
    isLoggedIn() {
      return this.$store.getters.isLoggedIn;
    },
    user() {
      return this.$store.getters.currentUser;
    },
    snackbarShow() {
      return this.$store.getters.snackbarShow;
    },
    snackbarText() {
      return this.$store.getters.snackbarText;
    },
  },
  data: () => ({
    // drawer: false,
  }),
  mounted: function () {
    this.$nextTick(function () {
      this.$store.dispatch("loadCurrentUser");
      const user = this.$store.getters.currentUser;

      if (user && user.access_token) {
        this.$store.commit("changeLoginState", true);
      }
    });
  },
  methods: {
    toggleDrawer() {
      const drawer = this.$store.getters.showDrawer;
      this.$store.commit("setShowDrawer", !drawer);
    },
  },
};
</script>
