import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import vuetify from "./plugins/vuetify";

Vue.config.productionTip = false;

import axios from 'axios'
var VueCookie = require('vue-cookie');
Vue.use(VueCookie);
new Vue({
  router,
  store,
  vuetify,
  render: (h) => h(App),
}).$mount("#app");

const base = axios.create({
  baseURL: 'http://localhost:8080/api/v1/'
});

Vue.prototype.$http = base;



import moment from 'moment'
Vue.prototype.$moment = moment;
