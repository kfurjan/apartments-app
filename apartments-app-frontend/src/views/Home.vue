<template>
  <div class="main-height" :class="{ 'overflow-hidden': !moveToTop }">
    <v-container
      fluid
      class="d-flex main-padding h-100 transition"
      :class="{ 'transform-background': moveToTop }"
    >
      <v-row>
        <div>
          <div class="background-image transition"></div>
          <div class="overlay transition"></div>
        </div>
        <v-col cols="12">
          <apartment-search
            class="transition"
            @searchClicked="searchApartments"
            :class="{ 'move-bottom': moveToTop }"
          ></apartment-search>
        </v-col>
      </v-row>
    </v-container>
    <v-container
      class="h-100 transition"
      justify="center"
      :class="{ 'transform-background': moveToTop }"
    >
      <!-- <v-row justify="center">
        <v-col cols="12" sm="6">
          <v-progress-linear
            indeterminate
            class="mt-5"
            color="orange darken-2"
          ></v-progress-linear>
        </v-col>
      </v-row> -->

      <v-row>
        <v-col cols="12">
          <apartment-list
            v-if="moveToTop"
            :city="city"
            :key="city"
          ></apartment-list>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<style scoped lang="scss">
@import "~vuetify/src/components/VStepper/_variables.scss";

.background-image {
  background: url("../assets/background.jpeg");
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  height: 100%;
  width: 100%;
  position: absolute;
  top: 0;
  left: 0;
}

.main-height {
  height: calc(100vh - 64px);
}

.overlay {
  background-color: black;
  position: absolute;
  top: 0;
  left: 0;
  height: 100%;
  width: 100%;
  opacity: 0.45;
}

.move-bottom {
  top: 95% !important;
  transform: none;
}

.transition {
  transition: all 1.3s ease-in-out;
}

.h-100 {
  height: 100%;
}

.h-100vh {
  height: 100vh;
}

.transform-background {
  transform: translateY(-81%);
}

.main-padding {
  padding: 80px;
}
</style>

<script>
import ApartmentSearch from "../components/ApartmentSearch";
import ApartmentList from "../components/ApartmentList";

export default {
  name: "Home",
  components: {
    ApartmentSearch,
    ApartmentList,
  },
  data: () => ({
    moveToTop: false,
    city: "",
  }),
  methods: {
    searchApartments({ city }) {
      this.moveToTop = true;
      this.city = city;
    },
  },
};
</script>
