<template>
  <div>
    <div v-if="apartments.length == 0">
      <p class="text-center">No results to show</p>
    </div>
    <div v-else>
      <h2 class="text-h2 my-4 text-center">Apartments</h2>
      <v-row justify="center">
        <v-col
          cols="12"
          l="4"
          md="6"
          v-for="apartment in apartments"
          v-bind:key="apartment.id"
          class="pa-3"
        >
          <apartment v-bind:apartment="apartment" />
        </v-col>
      </v-row>
    </div>
  </div>
</template>

<script>
import Apartment from "../components/Apartment";

export default {
  name: "ApartmentList",

  components: {
    Apartment,
  },
  data: () => ({
    apartments: {},
  }),
  props: ["city", "checkInDate", "checkOutDate"],
  methods: {
    showApartment(apartment) {
      console.log(apartment);
    },
  },
  mounted() {
    const db = require("../../db.json");
    this.apartments = db.apartments.filter((a) => a.city == this.$props.city);
  },
};
</script>
