<template>
  <v-card
    class="pa-6 pa-md-0 rounded-lg card-shape grey lighten-2 centered-card"
    align="center"
  >
    <v-row justify="center" align="center">
      <v-col cols="12" md="auto">
        <v-autocomplete
          ref="autocomplete"
          auto-select-first
          v-model="city"
          :items="cities"
          item-text="city"
          item-value="city"
          @input="citySelected"
          clearable
        ></v-autocomplete>
      </v-col>
      <v-col cols="12" md="auto">
        <v-menu
          v-model="showCheckInPicker"
          :close-on-content-click="true"
          :nudge-right="40"
          transition="scale-transition"
          offset-y
          min-width="auto"
        >
          <template v-slot:activator="{ on, attrs }">
            <v-text-field
              v-model="checkInFormatted"
              label="Check in date"
              prepend-icon="mdi-calendar"
              readonly
              v-bind="attrs"
              v-on="on"
            ></v-text-field>
          </template>
          <v-date-picker
            v-model="checkIn"
            :allowed-dates="checkInAllowedDates"
            @change="checkInSelected"
            show-adjacent-months
          ></v-date-picker>
        </v-menu>
      </v-col>
      <v-col cols="12" md="auto">
        <v-menu
          v-model="showCheckOutPicker"
          :close-on-content-click="true"
          :nudge-right="40"
          transition="scale-transition"
          offset-y
          min-width="auto"
        >
          <template v-slot:activator="{ on, attrs }">
            <v-text-field
              v-model="checkOutFormatted"
              label="Check out date"
              prepend-icon="mdi-calendar"
              readonly
              v-bind="attrs"
              v-on="on"
            ></v-text-field>
          </template>
          <v-date-picker
            v-model="checkOut"
            :allowed-dates="checkOutAllowedDates"
            show-adjacent-months
          ></v-date-picker>
        </v-menu>
      </v-col>
      <v-col cols="12" md="auto">
        <v-btn
          fab
          color="orange darken-4"
          outlined
          dark
          @click="searchApartments"
        >
          <v-icon dark> mdi-magnify </v-icon>
        </v-btn>
      </v-col>
    </v-row>
  </v-card>
</template>

<style lang="scss" scoped>
@import "~vuetify/src/components/VStepper/_variables.scss";

.card-shape {
  border-radius: map-get($rounded, "pill") !important;
}

.top-0 {
  top: 0% !important;
}

.centered-card {
  position: relative;
  top: 50%;
  transform: translateY(-50%);
}

@media #{map-get($display-breakpoints, 'sm-and-down')} {
  .card-shape {
    border-radius: map-get($rounded, "xl") !important;
  }
}
</style>

<script>
import moment from "moment";

export default {
  name: "ApartmentSearch",
  props: [],
  data: () => ({
    cities: [],
    city: null,
    checkIn: null,
    checkOut: null,
    showCheckOutPicker: false,
    showCheckInPicker: false,
  }),
  computed: {
    checkInFormatted: function () {
      const date = this.checkIn;
      return date ? this.formatDate(date) : null;
    },
    checkOutFormatted: function () {
      const date = this.checkOut;
      return date ? this.formatDate(date) : null;
    },
  },
  created() {
    this.cities = require("../../hr.json");
  },
  methods: {
    formatDate(date) {
      return moment(date).format("MMMM Do");
    },
    checkInAllowedDates(date) {
      return moment(date).isSameOrAfter(moment());
    },
    checkOutAllowedDates(date) {
      return moment(date).isSameOrAfter(this.checkIn);
    },
    searchApartments() {
      if (this.city && this.checkIn && this.checkOut) {
        this.$emit("searchClicked", {
          city: this.city,
          checkInDate: this.checkIn,
          checkOutDate: this.checkOut,
        });
      }

      if (!this.city) {
        this.$refs.autocomplete.focus();
        this.$refs.autocomplete.activateMenu();
      } else if (!this.checkIn) {
        this.showCheckInPicker = true;
      } else if (!this.checkOut) {
        this.showCheckOutPicker = true;
      }
    },
    citySelected() {
      if (this.checkIn == null) {
        this.showCheckInPicker = true;
      }
    },
    checkInSelected() {
      if (this.checkOut == null) {
        this.showCheckOutPicker = true;
      }
    },
  },
};
</script>
