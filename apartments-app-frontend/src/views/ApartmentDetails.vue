<template>
  <v-container>
    <v-row>
      <v-col cols="12">
        <p class="text-h3 mb-0">{{ apartment.title }}</p>
        <v-subheader class="pl-md-0">{{
          `${apartment.address}, ${apartment.postal_code} ${apartment.city}`
        }}</v-subheader>
      </v-col>
    </v-row>
    <v-row>
      <v-col cols="12" md="6">
        <v-img
          :aspect-ratio="1"
          max-height="100%"
          :src="require(`@/assets/${apartment.images[0]}`)"
        >
        </v-img>
      </v-col>
      <v-col cols="12" md="6">
        <v-row>
          <v-col
            cols="12"
            md="6"
            v-for="image in apartment.images.slice(1, 5)"
            :key="image"
          >
            <v-img
              :aspect-ratio="1"
              max-height="800px"
              :src="require(`@/assets/${image}`)"
            >
            </v-img>
          </v-col>
        </v-row>
      </v-col>
    </v-row>
    <v-divider class="mt-4"></v-divider>

    <v-row>
      <v-col cols="12" s="6" md="6" l="7" xl="8">
        <p class="text-justify pa-4">{{ apartment.description }}</p>
      </v-col>
      <v-col cols="12" md="auto">
        <v-card class="my-12" max-width="374" elevation="5">
          <v-card-title
            >{{ apartment.price_per_night }}€
            <span class="text-subtitle-2 pl-3 grey--text"> / per night</span>
          </v-card-title>

          <v-divider></v-divider>
          <v-card-text>
            <v-form ref="form">
              <v-row align="center" class="mx-0">
                <v-col cols="12" sm="6">
                  <v-menu
                    :close-on-content-click="true"
                    :nudge-right="40"
                    transition="scale-transition"
                    offset-y
                    min-width="auto"
                  >
                    <template v-slot:activator="{ on, attrs }">
                      <v-text-field
                        v-model="checkInFormatted"
                        label="Check in"
                        prepend-icon="mdi-calendar"
                        readonly
                        v-bind="attrs"
                        v-on="on"
                      ></v-text-field>
                    </template>
                    <v-date-picker
                      v-model="checkIn"
                      :allowed-dates="checkInAllowedDates"
                      show-adjacent-months
                    ></v-date-picker> </v-menu
                ></v-col>
                <v-col cols="12" sm="6">
                  <v-menu
                    :close-on-content-click="true"
                    :nudge-right="40"
                    transition="scale-transition"
                    offset-y
                    min-width="auto"
                  >
                    <template v-slot:activator="{ on, attrs }">
                      <v-text-field
                        v-model="checkOutFormatted"
                        label="Check out"
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
              </v-row>
              <v-row align="center" class="mx-0">
                <v-col cols="12">
                  <v-text-field
                    type="number"
                    :min="1"
                    label="Number of guests"
                    v-model="noOfGuests"
                    :rules="noOfGuestsRules"
                    required
                  ></v-text-field>
                </v-col>
              </v-row>
            </v-form>
            <v-divider class="mx-4"></v-divider>

            <v-list dense>
              <v-list-item>
                <v-list-item-content
                  ><v-list-item-title>Per night</v-list-item-title>
                </v-list-item-content>
                <v-list-item-action>
                  {{ apartment.price_per_night }}
                </v-list-item-action>
              </v-list-item>
              <v-list-item>
                <v-list-item-content
                  ><v-list-item-title>No of nights staying</v-list-item-title>
                </v-list-item-content>
                <v-list-item-action>
                  {{ nightsStaying }}
                </v-list-item-action>
              </v-list-item>
              <v-divider></v-divider>
              <v-list-item>
                <v-list-item-content
                  ><v-list-item-title>Total</v-list-item-title>
                </v-list-item-content>
                <v-list-item-action>
                  {{ totalPrice }}
                </v-list-item-action>
              </v-list-item>
            </v-list>
          </v-card-text>

          <v-card-actions>
            <v-btn block dark large color="red darken-4" @click="reserve">
              Reserve
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<style scoped lang="scss">
@import "~vuetify/src/components/VStepper/_variables.scss";
</style>

<script>
import repo from "../services/apiService";
import moment from "moment";

export default {
  name: "ApartmentDetails",
  components: {},
  data: () => ({
    apartment: {},
    checkIn: moment().format("YYYY-MM-DD"),
    checkOut: moment().add(2, "days").format("YYYY-MM-DD"),
    noOfGuests: 1,
    unavailableDates: [],
    noOfGuestsRules: [(u) => u > 0 || "Must be greater than 0"],
  }),
  async mounted() {
    // const id = this.$route.params.id;
    // const response = await api_service.get({ resource: "apartments", id });
    // this.apartment = await response.json();
    const db = require("../../db.json");
    this.apartment = db.apartments.find((a) => a.id == this.$route.params.id);

    const user = this.$store.getters.currentUser;

    const resource = `apartments/${this.$route.params.id}/unavailable_dates`;
    this.unavailableDates = (
      await repo.get({ resource, token: user.access_token })
    ).data;
  },
  methods: {
    formatDate(date) {
      return moment(date).format("DD/MM/yyyy");
    },
    checkInAllowedDates(date) {
      return (
        moment(date).isSameOrAfter(moment()) &&
        !this.unavailableDates.includes(date)
      );
    },
    checkOutAllowedDates(date) {
      return (
        moment(date).isSameOrAfter(this.checkIn) &&
        !this.unavailableDates.includes(date)
      );
    },
    async reserve() {
      const valid = this.$refs.form.validate();

      if (!valid) {
        return;
      }

      const user = this.$store.getters.currentUser;
      const data = {
        guest_id: user.roleId,
        apartment_id: this.apartment.id,
        number_of_guests: this.noOfGuests,
        starts_at: moment(this.checkIn).format("yyyy-MM-DDT09:00:00"),
        ends_at: moment(this.checkOut).format("yyyy-MM-DDT09:00:00"),
      };
      try {
        await repo.post({
          resource: "reservations",
          token: user.access_token,
          body: data,
        });

        this.$router.push("/");
      } catch (error) {
        console.log(error);
      }
    },
  },
  computed: {
    totalPrice() {
      return this.apartment.price_per_night * this.nightsStaying;
    },
    nightsStaying() {
      return moment(this.checkOut).diff(this.checkIn, "days");
    },
    checkInFormatted: function () {
      const date = this.checkIn;
      return date ? this.formatDate(date) : null;
    },
    checkOutFormatted: function () {
      const date = this.checkOut;
      return date ? this.formatDate(date) : null;
    },
  },
};
</script>
