<template>
  <v-container>
    <v-data-table
      :headers="headers"
      :items="reservations"
      class="elevation-1 mt-6"
      hide-default-footer
    >
      <template v-slot:item.starts_at="{ item }">
        {{ formatDate(item.starts_at) }}
      </template>
      <template v-slot:item.ends_at="{ item }">
        {{ formatDate(item.ends_at) }}
      </template>
    </v-data-table>
  </v-container>
</template>

<script>
import repo from "../services/apiService";
import moment from "moment";

export default {
  data: () => ({
    reservations: [],
    headers: [
      {
        text: "Number of guests",
        value: "number_of_guests",
      },
      { text: "Starts at", value: "starts_at" },
      { text: "Ends at", value: "ends_at" },
    ],
  }),
  methods: {
    formatDate(date) {
      return moment(date).format("DD/MM/yyyy hh:mm");
    },
  },
  async mounted() {
    const user = this.$store.getters.currentUser;
    this.reservations = (
      await repo.get({ resource: "reservations", token: user.access_token })
    ).data;
  },
};
</script>
