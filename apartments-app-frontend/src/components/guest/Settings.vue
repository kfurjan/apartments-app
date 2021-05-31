<template>
  <v-container fluid>
    <v-layout align-center justify-center>
      <v-flex xs12 sm8 md4>
        <v-alert
          class="mt-4"
          type="error"
          v-model="showAlert"
          dismissible
          transition="slide-y-transition"
          outlined
        >
          {{ alertText }}
        </v-alert>
        <v-card class="">
          <v-toolbar dark color="primary">
            <v-toolbar-title></v-toolbar-title>
          </v-toolbar>
          <v-form ref="form" lazy-validation @submit.prevent="submit">
            <v-card-text>
              <v-text-field
                name="firstName"
                type="text"
                label="First name"
                v-model="firstName"
                :rules="firstNameRules"
                required
              ></v-text-field>
              <v-text-field
                name="lastName"
                type="text"
                label="Last name"
                v-model="lastName"
                :rules="lastNameRules"
                required
              ></v-text-field>
              <v-text-field
                name="oib"
                type="text"
                label="OIB"
                v-model="oib"
                :rules="oibRules"
                required
              ></v-text-field>
              <v-menu
                :close-on-content-click="false"
                :nudge-right="40"
                transition="scale-transition"
                offset-y
                min-width="auto"
              >
                <template v-slot:activator="{ on, attrs }">
                  <v-text-field
                    v-model="dateOfBirth"
                    label="Date of birth"
                    prepend-icon="mdi-calendar"
                    readonly
                    v-bind="attrs"
                    v-on="on"
                  ></v-text-field>
                </template>
                <v-date-picker
                  v-model="dateOfBirth"
                  show-adjacent-months
                ></v-date-picker>
              </v-menu>
            </v-card-text>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn color="primary" type="submit">{{ mode }}</v-btn>
            </v-card-actions>
          </v-form>
        </v-card>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import settingsService from "../../services/settingsService";

export default {
  name: "RenterSettings",
  data() {
    return {
      firstName: "",
      lastName: "",
      oib: "",
      dateOfBirth: "",
      address: "",
      city: "",
      firstNameRules: [(u) => !!u || "First name is required"],
      lastNameRules: [(u) => !!u || "Last name is required"],
      oibRules: [(u) => !!u || "OIB is required"],
      dateOfBirthRules: [(u) => !!u || "Date of birth is required"],
      showAlert: false,
      alertText: "",
    };
  },
  methods: {
    async submit() {
      const valid = this.$refs.form.validate();

      if (!valid) {
        return;
      }

      const data = {
        first_name: this.firstName,
        last_name: this.lastName,
        oib: this.oib,
        date_of_birth: this.dateOfBirth,
        user_id: this.$store.getters.currentUser.id,
      };

      const handler =
        this.mode == "Create"
          ? settingsService.createUser
          : settingsService.updateUser;

      try {
        const user = this.$store.getters.currentUser;
        const result = await handler(data, user, "guests");

        if (!user.roleId) {
          user.roleId = result.data.id;
          this.$cookie.set("user", JSON.stringify(user), 1);
        }
        this.$router.push("/");
      } catch (error) {
        const errors = error.response.data.errors;
        this.showAlert = true;
        this.alertText = errors[0];
      }
    },
  },
  computed: {
    mode() {
      const user = this.$store.getters.currentUser;
      const userHasInfo = !!user.roleId;
      return userHasInfo ? "Update" : "Create";
    },
  },
  async mounted() {
    if (this.mode == "Create") {
      this.alertText = "Please fill in your personal information";
      this.showAlert = true;
    } else {
      const user = this.$store.getters.currentUser;
      const settings = (await settingsService.getSettings(user)).data;

      this.firstName = settings.first_name;
      this.lastName = settings.last_name;
      this.oib = settings.oib;
      this.dateOfBirth = settings.date_of_birth;
    }
  },
};
</script>
