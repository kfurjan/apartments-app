import repo from './apiService'

export default {
  async loginUser(vue, res) {
    const user = {
      access_token: res.data.access_token,
    };

    const userInfo = await repo.get({ resource: "user", token: user.access_token });

    user.email = userInfo.data.email;
    user.role = userInfo.data.role;

    if (userInfo.data.renter_id) {
      user.roleId = userInfo.data.renter_id;
    } else if (userInfo.data.guest_id) {
      user.roleId = userInfo.data.guest_id;
    }

    vue.$cookie.set("user", JSON.stringify(user), 1);
    vue.$store.dispatch("loadCurrentUser");
    vue.$store.commit("changeLoginState", true);
    vue.$router.push("/");
  }
}
