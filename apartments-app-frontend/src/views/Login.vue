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
            <v-toolbar-title>Login</v-toolbar-title>
          </v-toolbar>
          <v-form ref="form" lazy-validation @submit.prevent="login">
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
            </v-card-text>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn color="primary" type="submit">Login</v-btn>
            </v-card-actions>
          </v-form>
        </v-card>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import repo from "../services/apiService";
import login_service from "../services/loginService";

export default {
  name: "Login",
  data() {
    return {
      email: "",
      emailRules: [(u) => !!u || "Email is required"],
      passwordRules: [(u) => !!u || "Password is required"],
      password: "",
      showAlert: false,
      alertText: "",
    };
  },
  methods: {
    login: function () {
      const valid = this.$refs.form.validate();

      if (!valid) {
        return;
      }

      repo
        .post({
          resource: `authentication/login`,
          body: {
            email: this.email,
            password_digest: this.password,
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
    logout: function () {},
  },
};
</script>
