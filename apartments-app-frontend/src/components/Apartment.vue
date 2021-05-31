<template>
  <v-card class="mb-4 p-3" height="100%" elevation="2" @click="showApartment">
    <v-carousel hide-delimiter-background show-arrows-on-hover>
      <v-carousel-item
        v-for="image in apartment.images"
        :key="image"
        :src="require(`@/assets/${image}`)"
        width="auto"
        aspect-ratio="1"
      >
      </v-carousel-item>
    </v-carousel>
    <v-card-title>{{ apartment.title }}</v-card-title>

    <v-card-text>
      <v-row align="center" class="mx-0">
        <v-rating
          :value="apartment.rating"
          color="amber"
          dense
          half-increments
          readonly
          size="14"
        ></v-rating>

        <div class="grey--text ms-4">
          {{ apartment.rating }} ({{ Math.floor(Math.random() * 200 + 100) }})
        </div>
      </v-row>

      <div class="my-4 subtitle-1">
        <v-row class="mx-0" align="center">
          <div>{{ apartment.price_per_night }}€ / per night</div>
          <v-spacer></v-spacer>
          <div class="d-flex align-center">
            <v-icon color="teal darken-2">mdi-map-marker</v-icon>
            {{ apartment.city }}
          </div>
        </v-row>
      </div>

      <div class="pt-2">{{ apartment.description.slice(0, 200) }}...</div>
    </v-card-text>
  </v-card>
</template>

<script>
export default {
  name: "Apartment",
  props: ["apartment"],
  methods: {
    showApartment() {
      const apartment = this.$props.apartment;
      this.$router.push({ name: "Apartment", params: { id: apartment.id } });
    },
  },
};
</script>
