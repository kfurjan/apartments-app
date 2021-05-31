<template>
  <v-navigation-drawer
    v-model="showDrawer"
    fixed
    temporary
    dark
    v-if="isLoggedIn"
  >
    <v-list>
      <v-list-item>
        <v-list-item-content>
          <v-list-item-title class="text-h6">
            {{ user.email }}
          </v-list-item-title>
          <v-list-item-subtitle>{{ user.role }}</v-list-item-subtitle>
        </v-list-item-content>
      </v-list-item>
    </v-list>

    <v-divider></v-divider>

    <template v-if="role == 'guest'">
      <guest-navigation></guest-navigation>
    </template>
    <template v-else>
      <renter-navigation></renter-navigation>
    </template>

    <template v-slot:append>
      <div class="pa-2">
        <v-btn block @click="logout"> Logout </v-btn>
      </div>
    </template>
  </v-navigation-drawer>
</template>

<script>
import GuestNavigation from "./guest/Navigation.vue";
import RenterNavigation from "./renter/Navigation.vue";

export default {
  name: "Navigation",
  components: {
    GuestNavigation,
    RenterNavigation,
  },
  computed: {
    isLoggedIn() {
      return this.$store.getters.isLoggedIn;
    },
    role() {
      return this.user.role;
    },
    user() {
      return this.$store.getters.currentUser;
    },
    showDrawer: {
      get() {
        return this.$store.getters.showDrawer;
      },
      set(val) {
        this.$store.commit("setShowDrawer", val);
      },
    },
  },
  methods: {
    logout: function () {
      this.$http
        .post(`authentication/logout`, null, {
          headers: {
            authorization: `Bearer ${this.user.access_token}`,
          },
        })
        .then((res) => {
          console.log(res);
        })
        .catch((error) => {
          const errors = error.response.data.errors;

          console.log(errors);
        });
      this.$store.commit("changeLoginState", false);
      this.$cookie.delete("user");
      // this.$store.commit("setSnackbarText", "Logged out.");
      // this.$store.commit("setSnackbarShow", true);
      this.$store.commit("setShowDrawer", false);
      this.$router.push("/");
    },
  },
};
</script>
