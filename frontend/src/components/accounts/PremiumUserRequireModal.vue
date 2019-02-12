<template>
  <v-dialog
      v-model="dialog"
      max-width="500"
  >
    <v-card>
      <v-card-title class="headline">
        {{t("You need to be a premium user to see details. Do you want to become one?")}}
      </v-card-title>

      <v-card-text>
       {{t("You can become a primary use by subscribing only for 5$ per month. You will be able to see water place statisctics and detailed data.")}}
      </v-card-text>

      <v-card-actions>
        <v-spacer></v-spacer>

        <v-btn
            color="red darken-1"
            flat="flat"
            @click="$emit('closed', false)"
        >
          {{t("Decline")}}
        </v-btn>

        <v-btn
            color="green darken-1"
            flat="flat"
            @click="$emit('closed', true)"
        >
          {{t("Subscribe")}}
        </v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script>
export default {
  name: 'PremiumUserRequireModal',
  data () {
    return {
      dialog: true
    }
  }
}
</script>

<style scoped>

</style>
