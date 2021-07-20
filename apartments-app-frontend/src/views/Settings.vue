<template>
  <div>
    <template v-if="userRole == 'renter'">
      <renter-settings />
    </template>
    <template v-else>
      <guest-settings />
    </template>
    <v-container fluid>
      <v-layout align-center justify-center>
        <v-dialog v-model="dialog" width="500">
          <template v-slot:activator="{ on, attrs }">
            <v-btn color="red lighten-2" dark v-bind="attrs" v-on="on">
              Delete account
            </v-btn>
          </template>

          <v-card>
            <v-card-title class="text-h5 red lighten-2 mb-4">
              Delete account
            </v-card-title>

            <v-card-text>
              Are you sure you want to delete your account and all of your
              personal data? This action is irreversible.
            </v-card-text>

            <v-divider></v-divider>

            <v-card-actions>
              <v-btn color="error" text @click="deleteAccount"> Delete </v-btn>
              <v-spacer></v-spacer>
              <v-btn color="primary" text @click="dialog = false">
                Cancel
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>
      </v-layout>
    </v-container>
  </div>
</template>

<script>
import GuestSettings from "../components/guest/Settings.vue";
import RenterSettings from "../components/renter/Settings.vue";
import repo from "../services/apiService";

export default {
  name: "Settings",
  components: { GuestSettings, RenterSettings },
  data() {
    return {
      dialog: false,
    };
  },
  computed: {
    userRole() {
      return this.$store.getters.currentUser.role;
    },
  },
  methods: {
    async deleteAccount() {
      const user = this.$store.getters.currentUser;

      try {
        (
          await repo.delete({
            resource: "users",
            id: user.id,
            token: user.access_token,
          })
        ).data;
      } catch (error) {
        console.log(error);
      }
    },
  },
};
</script>
