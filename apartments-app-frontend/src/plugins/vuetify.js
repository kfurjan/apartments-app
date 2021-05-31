import Vue from "vue";
import Vuetify from "vuetify/lib/framework";

Vue.use(Vuetify);

export default new Vuetify({
  theme: {
    themes: {
      dark: {
        primary: '#1b1e29',
        secondary: '#f74a65',
        accent: '#2c2f3e',
        error: '#b71c1c',
      },
    },
  },
});
