import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    isLoggedIn: false,
    snackbarText: '',
    snackbarShow: false,
    showDrawer: false,
    currentUser: {}
  },
  mutations: {
    changeLoginState(state, isLoggedIn) {
      state.isLoggedIn = isLoggedIn
    },
    setSnackbarText(state, text) {
      state.snackbarText = text
    },
    setSnackbarShow(state, show) {
      state.snackbarShow = show
    },
    setShowDrawer(state, show) {
      state.showDrawer = show
    },
    setCurrentUser(state, user) {
      state.currentUser = user
    }
  },
  getters: {
    isLoggedIn: state => state.isLoggedIn,
    snackbarText: state => state.snackbarText,
    snackbarShow: state => state.snackbarShow,
    showDrawer: state => state.showDrawer,
    currentUser: state => state.currentUser,
  },
  actions: {
    loadCurrentUser: ({ commit }) => {
      const user = JSON.parse(Vue.prototype.$cookie.get("user"));
      commit('setCurrentUser', user)
    }
  },
  modules: {},
});
