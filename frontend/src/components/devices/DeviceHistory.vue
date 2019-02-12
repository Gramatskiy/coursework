<template>
  <v-flex class="xs12 md2">
    <v-list dense>
      <v-subheader>
        {{t("Saved places")}}
      </v-subheader>
      <template v-if="devices.length > 0">
        <v-list-tile v-for="(device, index) in devices" v-if="$store.state.savedDevices.includes(device.id)"
                     @click="$emit('deviceClicked', device)" :key="index" class="pb-2 v-card--hover active">
          <v-list-tile-avatar>
            <img :src="device.photo">
          </v-list-tile-avatar>
          <v-list-tile-content>
            <v-list-tile-title> {{device.name}}</v-list-tile-title>
            <v-list-tile-sub-title>{{device.description}}</v-list-tile-sub-title>
          </v-list-tile-content>
          <v-list-tile-action>
            <v-chip color="blue" text-color="white"> {{parseFloat(device.measurements.temperature)}} °C</v-chip>
          </v-list-tile-action>
        </v-list-tile>
      </template>
      <h4 v-else class="ml-3" >{{t("No saved places yet")}}</h4>
    </v-list>
  </v-flex>
</template>

<script>

export default {
  name: 'DeviceHistory',
  props: ['devices']
}
</script>

<style scoped>

</style>
