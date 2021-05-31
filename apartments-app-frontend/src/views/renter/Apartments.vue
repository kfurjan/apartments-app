<template>
  <v-container>
    <div class="mb-3">
      <v-btn
        depressed
        color="primary"
        light
        @click="$router.push('/renter/apartments/new')"
      >
        New apartment</v-btn
      >
    </div>
    <v-data-iterator
      disable-pagination
      hide-default-footer
      :items="apartments"
      :search="search"
      :sort-by="sortBy.toLowerCase()"
      :sort-desc="sortDesc"
    >
      <template v-slot:header>
        <v-toolbar dark color="grey darken-3" class="mb-1">
          <v-text-field
            v-model="search"
            clearable
            flat
            solo-inverted
            hide-details
            prepend-inner-icon="mdi-magnify"
            label="Search by title"
          ></v-text-field>
          <template v-if="$vuetify.breakpoint.mdAndUp">
            <v-spacer></v-spacer>
            <v-select
              v-model="sortBy"
              flat
              solo-inverted
              hide-details
              :items="sortValues"
              prepend-inner-icon="mdi-magnify"
              label="Sort by"
            ></v-select>
            <v-spacer></v-spacer>
            <v-btn-toggle v-model="sortDesc" mandatory>
              <v-btn large depressed color="grey darken-3" :value="false">
                <v-icon>mdi-arrow-up</v-icon>
              </v-btn>
              <v-btn large depressed color="grey darken-3" :value="true">
                <v-icon>mdi-arrow-down</v-icon>
              </v-btn>
            </v-btn-toggle>
          </template>
        </v-toolbar>
      </template>
      <template v-slot:default="props">
        <v-row dense>
          <v-col v-for="item in props.items" :key="item.id" cols="12" md="6">
            <v-card color="grey lighten-3">
              <div
                class="d-flex flex-no-wrap justify-space-between align-center"
              >
                <v-avatar class="ma-3" size="145" tile>
                  <v-img :src="require(`@/assets/${item.images[0]}`)"></v-img>
                </v-avatar>
                <div>
                  <v-card-title class="text-h5">
                    {{ item.title }}
                  </v-card-title>
                  <v-card-subtitle class="d-flex">
                    {{ item.price_per_night }}€ / night
                    <v-spacer></v-spacer>
                    {{ item.city }}
                  </v-card-subtitle>
                  <v-card-text class="px-4">
                    {{ item.description.slice(0, 200) }}...
                  </v-card-text>
                  <v-card-actions class="d-flex">
                    <v-btn
                      depressed
                      color="success"
                      light
                      @click="
                        $router.push(`/renter/apartments/${item.id}/edit`)
                      "
                    >
                      Edit
                    </v-btn>
                    <v-spacer></v-spacer>
                    <v-btn text color="error"> Delete </v-btn>
                  </v-card-actions>
                </div>
              </div>
            </v-card>
          </v-col>
        </v-row>
      </template>
    </v-data-iterator>
  </v-container>
</template>

<style scoped lang="scss">
@import "~vuetify/src/components/VStepper/_variables.scss";
</style>

<script>
// import ApartmentSearch from "../components/ApartmentSearch";
// import ApartmentList from "../components/ApartmentList";

export default {
  name: "Apartments",
  components: {
    // ApartmentList,
  },
  data: () => ({
    moveToTop: false,
    city: "",
    apartments: [],
    sortBy: "title",
    sortValues: ["Title", "Price_per_night", "City"],
    sortDesc: false,
    search: "",
  }),
  methods: {
    searchByTitle(searchTerm) {
      this.apartments.filter((a) => a.title.includes(searchTerm));
    },
  },
  mounted() {
    const db = require("../../../db.json");
    this.apartments = db.apartments.slice(0, 2);
  },
};
</script>
