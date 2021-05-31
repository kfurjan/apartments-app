<template>
  <div>
    <template v-if="userRole == 'renter'">
      <renter-settings />
    </template>
    <template v-else>
      <guest-settings />
    </template>
  </div>
</template>

<script>
import GuestSettings from "../components/guest/Settings.vue";
import RenterSettings from "../components/renter/Settings.vue";

export default {
  name: "Settings",
  components: { GuestSettings, RenterSettings },
  data() {
    return {};
  },
  computed: {
    userRole() {
      return this.$store.getters.currentUser.role;
    },
  },
  methods: {},
};
</script>
