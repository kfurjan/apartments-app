<template>
  <v-container>
    <v-form>
      <v-text-field
        v-model="title"
        :rules="titleRules"
        label="Title"
        required
      ></v-text-field>
      <v-textarea
        v-model="description"
        :rules="descriptionRules"
        label="Description"
        required
      ></v-textarea>
      <v-text-field
        v-model="pricePerNight"
        :rules="pricePerNightRules"
        type="number"
        label="Price per night"
        required
      ></v-text-field>
      <v-row>
        <v-col cols="12" md="4">
          <v-text-field
            v-model="address"
            :rules="addressRules"
            label="Address"
            required
          ></v-text-field>
        </v-col>
        <v-col cols="12" md="4">
          <v-text-field
            v-model="city"
            :rules="cityRules"
            label="City"
            required
          ></v-text-field>
        </v-col>
        <v-col cols="12" md="4">
          <v-text-field
            v-model="postalCode"
            :rules="postalCodeRules"
            label="Postal code"
            required
          ></v-text-field>
        </v-col>
      </v-row>
      <v-row>
        <v-col cols="12" md="6">
          <v-menu
            :close-on-content-click="true"
            :nudge-right="40"
            transition="scale-transition"
            offset-y
            min-width="auto"
          >
            <template v-slot:activator="{ on, attrs }">
              <v-text-field
                v-model="availabilityStartDate"
                label="Availability start date"
                prepend-icon="mdi-calendar"
                :rules="availabilityStartDateRules"
                readonly
                v-bind="attrs"
                v-on="on"
              ></v-text-field>
            </template>
            <v-date-picker
              v-model="availabilityStartDate"
              show-adjacent-months
            ></v-date-picker>
          </v-menu>
        </v-col>
        <v-col cols="12" md="6">
          <v-menu
            :close-on-content-click="true"
            :nudge-right="40"
            transition="scale-transition"
            offset-y
            min-width="auto"
          >
            <template v-slot:activator="{ on, attrs }">
              <v-text-field
                v-model="availabilityEndDate"
                label="Availability end date"
                prepend-icon="mdi-calendar"
                :rules="availabilityEndDateRules"
                readonly
                v-bind="attrs"
                v-on="on"
              ></v-text-field>
            </template>
            <v-date-picker
              v-model="availabilityEndDate"
              show-adjacent-months
            ></v-date-picker>
          </v-menu>
        </v-col>
      </v-row>
      <v-btn color="primary" class="mt-4" @click="submitForm">{{
        $props.mode
      }}</v-btn>
    </v-form>
  </v-container>
</template>

<script>
import apartmentsService from "../../services/apartmentsService";

export default {
  data: () => ({
    id: "",
    title: "",
    description: "",
    pricePerNight: "",
    address: "",
    city: "",
    postalCode: "",
    availabilityStartDate: "",
    availabilityEndDate: "",
    titleRules: [(u) => !!u || "Required"],
    pricePerNightRules: [(u) => !!u || "Required"],
    addressRules: [(u) => !!u || "Required"],
    cityRules: [(u) => !!u || "Required"],
    postalCodeRules: [(u) => !!u || "Required"],
    descriptionRules: [(u) => !!u || "Required"],
    availabilityStartDateRules: [(u) => !!u || "Required"],
    availabilityEndDateRules: [(u) => !!u || "Required"],
  }),
  props: ["mode"],
  async mounted() {
    if (this.$props.mode == "Update") {
      const user = this.$store.getters.currentUser;
      const apartment = (
        await apartmentsService.getApartment(user, this.$route.params.id)
      ).data;

      this.id = this.$route.params.id;
      this.title = apartment.title;
      this.description = apartment.description;
      this.pricePerNight = apartment.price_per_night;
      this.address = apartment.address;
      this.city = apartment.city;
      this.postalCode = apartment.postal_code;
      this.availabilityStartDate = apartment.availability_start_date;
      this.availabilityEndDate = apartment.availability_end_date;
    }
  },
  methods: {
    async submitForm() {
      const user = this.$store.getters.currentUser;
      const data = {
        title: this.title,
        description: this.description,
        price_per_night: this.pricePerNight,
        address: this.address,
        city: this.city,
        postal_code: this.postalCode,
        available: true,
        availability_start_date: this.availabilityStartDate,
        availability_end_date: this.availabilityEndDate,
        renter_id: user.roleId,
      };

      try {
        if (this.$props.mode == "Update") {
          await apartmentsService.updateApartment(data, user, this.id);
        } else if (this.$props.mode == "Create") {
          await apartmentsService.createApartment(data, user);
        }

        this.$router.push("/renter/apartments");
      } catch (error) {
        console.log(error);
      }
    },
  },
};
</script>
