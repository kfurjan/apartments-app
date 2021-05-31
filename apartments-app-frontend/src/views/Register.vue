<template>
  <v-container fluid>
    <v-layout align-center justify-center>
      <v-flex xs12 sm8 md4>
        <v-alert
          class="mt-4"
          type="error"
          v-model="showAlert"
          transition="slide-y-transition"
          dismissible
          outlined
        >
          {{ alertText }}
        </v-alert>
        <v-card class="">
          <v-toolbar dark color="primary">
            <v-toolbar-title>Register</v-toolbar-title>
          </v-toolbar>
          <v-form ref="form" lazy-validation @submit.prevent="register">
            <v-card-text>
              <v-text-field
                prepend-icon="mdi-account"
                name="email"
                type="text"
                label="Email"
                v-model="email"
                :rules="emailRules"
                required
              ></v-text-field>
              <v-text-field
                id="password"
                prepend-icon="mdi-lock"
                name="password"
                label="Password"
                type="password"
                v-model="password"
                :rules="passwordRules"
                required
              ></v-text-field>
              <v-text-field
                id="confirmPassword"
                prepend-icon="mdi-lock"
                name="confirmPassword"
                label="Confirm password"
                type="password"
                v-model="confirmPassword"
                :rules="confirmPasswordRules"
                required
              ></v-text-field>
              <v-radio-group v-model="role" mandatory row>
                <v-radio label="Guest" value="guest"></v-radio>
                <v-radio label="Renter" value="renter"></v-radio>
              </v-radio-group>
            </v-card-text>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn color="primary" type="submit">Register</v-btn>
            </v-card-actions>
          </v-form>
        </v-card>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import login_service from "../services/loginService";
import repo from "../services/apiService";

export default {
  name: "Register",
  data() {
    return {
      email: "",
      emailRules: [(u) => !!u || "Email is required"],
      password: "",
      passwordRules: [(u) => !!u || "Password is required"],
      confirmPassword: "",
      confirmPasswordRules: [
        (u) => !!u || "Confirm password is required",
        (u) =>
          u == this.password || "The password confirmation does not match.",
      ],
      role: "guest",
      showAlert: false,
      alertText: "",
    };
  },
  methods: {
    register: function () {
      const valid = this.$refs.form.validate();

      if (!valid) {
        return;
      }

      repo
        .post({
          resource: `user`,
          body: {
            email: this.email,
            password_digest: this.password,
            role: this.role,
          },
        })
        .then(async (res) => {
          await login_service.loginUser(this, res);
        })
        .catch((error) => {
          const errors = error.response.data.errors;
          this.showAlert = true;
          this.alertText = errors[0];

          console.log(errors);
        });
    },
  },
};
</script>
