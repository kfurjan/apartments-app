<template>
  <v-list nav dense>
    <v-list-item link @click="$router.push('/settings')">
      <v-list-item-icon>
        <v-icon>mdi-cog</v-icon>
      </v-list-item-icon>
      <v-list-item-title>Settings</v-list-item-title>
    </v-list-item>
    <v-list-item link @click="$router.push('/reservations')">
      <v-list-item-icon>
        <v-icon>mdi-file</v-icon>
      </v-list-item-icon>
      <v-list-item-title>Reservations</v-list-item-title>
    </v-list-item>
    <v-list-item link>
      <v-list-item-icon>
        <v-icon>mdi-receipt</v-icon>
      </v-list-item-icon>
      <v-list-item-title>Receipts</v-list-item-title>
    </v-list-item>
  </v-list>
</template>

<script>
export default {
  name: "GuestNavigation",
};
</script>
