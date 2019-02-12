<template>
  <v-flex v-if="device" class="xs12 md3">
    <v-card>
      <v-img
          :src="device.photo"
          aspect-ratio="2.75"
      ></v-img>

      <v-card-title primary-title>
        <div>
          <v-layout row align-center>
            <h2 class="headline mb-0">{{device.name}}</h2>
            <div class="ml-2 grey--text">
              {{t("last update")}}
              ({{device.measurements.timestamp|moment('LLL')}})
            </div>
          </v-layout>
          <h4>{{device.description}}</h4>
          <div>
            {{t("Amount is")}}
            {{getTemperatureDisplay}} С
          </div>
          <template v-if="$store.state.isPremium">
            <div>
              {{t("Turbidity is")}}
              {{this.device.measurements.turbidity}}
            </div>
            <div>
              {{t("PH level is")}}
              {{this.device.measurements.ph_level}}
            </div>
            <div>
              {{t("Gyroscope is")}}
              {{this.device.measurements.gyroscope}}
            </div>
            <div>
              {{t("Accelerator is")}}
              {{this.device.measurements.accelerator}}
            </div>
            <div>
              {{t("Magnetometer is")}}
              {{this.device.measurements.magnetometer}}
            </div>
          </template>
        </div>
      </v-card-title>
      <v-card-actions>
        <v-btn flat color="green" v-if="!$store.state.savedDevices.includes(device.id)"
               @click="addSavedDevice(device.id)">{{t("Save")}}
        </v-btn>
        <v-btn flat color="red" v-else @click="removeSavedDevice(device.id)">{{t("Remove from saved")}}</v-btn>
        <v-btn flat color="orange" v-if="!$store.state.isPremium" @click="showPremiumUserModal=true">{{t("See details")}}</v-btn>
        <v-btn flat color="success" v-else
               @click="$router.push({'name':'client-device-statistics', 'params':{'id':device.id}})">{{t("Update")}}
        </v-btn>
      </v-card-actions>
    </v-card>
    <premium-user-require-modal v-if="showPremiumUserModal" @closed="handleAnswer"></premium-user-require-modal>
  </v-flex>
</template>

<script>
import { mapActions } from 'vuex'
import PremiumUserRequireModal from '../accounts/PremiumUserRequireModal'

export default {
  name: 'DeviceMapDetail',
  components: { PremiumUserRequireModal },
  props: ['device'],
  data () {
    return {
      showPremiumUserModal: false
    }
  },
  computed: {
    getTemperatureDisplay () {
      return parseFloat(this.device.measurements.temperature).toFixed(2)
    }
  },
  methods: {
    ...mapActions(['addSavedDevice', 'removeSavedDevice']),
    handleAnswer (answer) {
      this.showPremiumUserModal = false
      if (answer) {
        this.$router.push({ name: 'subscribe-premium' })
      }
    }
  }
}
</script>

<style scoped>

</style>
