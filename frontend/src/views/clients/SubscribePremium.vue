<template>
  <v-stepper v-model="step">
    <v-stepper-header>
      <v-stepper-step :complete="step > 1" step="1" color="green">{{t('Select type')}}</v-stepper-step>

      <v-divider></v-divider>

      <v-stepper-step :complete="step > 2" step="2" color="green">{{t('Enter your data')}}</v-stepper-step>

      <v-divider></v-divider>

    </v-stepper-header>

    <v-stepper-items>
      <v-stepper-content step="1">
        <v-layout d-flex justify-center align-center class="column text-xs-center">
          <h1>{{t('MagnitHouse premium')}}</h1>
          <h5>{{t('Get more details')}}</h5>
          <v-flex d-flex class="flex row">
            <v-card width="250" class="mt-5">
              <v-card-title class="justify-center"><h4>{{t('No premium')}}</h4></v-card-title>
              <v-divider></v-divider>
              <v-list dense>
                <v-list-tile>
                  <v-list-tile-content>{{t('Data:')}}</v-list-tile-content>
                  <v-list-tile-content class="align-end">{{t('temperature')}}</v-list-tile-content>
                </v-list-tile>
                <v-list-tile>
                  <v-list-tile-content>{{t('Saved places:')}}</v-list-tile-content>
                  <v-list-tile-content class="align-end">{{t('yes')}}</v-list-tile-content>
                </v-list-tile>
                <v-list-tile>
                  <v-list-tile-content>Notifications:</v-list-tile-content>
                  <v-list-tile-content class="align-end">{{t('Yes')}}</v-list-tile-content>
                </v-list-tile>
                <v-list-tile>
                  <v-list-tile-content>Price:</v-list-tile-content>
                  <v-list-tile-content class="align-end">{{t('Free')}}</v-list-tile-content>
                </v-list-tile>
              </v-list>
            </v-card>

            <v-card width="350" class="ma-2" hover @click="handleTypeSelect($options.MONTH_12)">
              <v-card-title class="justify-center"><h4>{{t('12 months')}}</h4></v-card-title>
              <v-divider></v-divider>
              <v-list dense>
                <v-list-tile>
                  <v-list-tile-content>{{t('Data:')}}</v-list-tile-content>
                  <v-list-tile-content class="align-end">{{t('temperature, turbidity, ph level')}}</v-list-tile-content>
                </v-list-tile>
                <v-list-tile>
                  <v-list-tile-content>{{t('Saved places:')}}</v-list-tile-content>
                  <v-list-tile-content class="align-end">{{t('yes')}}</v-list-tile-content>
                </v-list-tile>
                <v-list-tile>
                  <v-list-tile-content>{{t('Notifications:')}}</v-list-tile-content>
                  <v-list-tile-content class="align-end">{{t('Yes')}}</v-list-tile-content>
                </v-list-tile>
                <v-list-tile>
                  <v-list-tile-content>{{t('Statistics:')}}</v-list-tile-content>
                  <v-list-tile-content class="align-end">{{t('Yes')}}</v-list-tile-content>
                </v-list-tile>
                <v-list-tile>
                  <v-list-tile-content>{{t('Price:')}}</v-list-tile-content>
                  <v-list-tile-content class="align-end">{{t('10$ per year')}}</v-list-tile-content>
                </v-list-tile>
                <v-card-actions class="justify-center">
                  <v-btn color="success" text-color="white" @click="handleTypeSelect($options.MONTH_12)">
                    {{t('Select')}}
                  </v-btn>
                </v-card-actions>

              </v-list>
            </v-card>
            <v-card width="250" class="mt-4" hover @click="handleTypeSelect($options.MONTH_1)">
              <v-card-title class="justify-center"><h4>{{t('1 month')}}</h4></v-card-title>
              <v-divider></v-divider>
              <v-list dense>
                <v-list-tile>
                  <v-list-tile-content>{{t('Data:')}}</v-list-tile-content>
                  <v-list-tile-content class="align-end">{{t('temperature, turbidity, ph level')}}</v-list-tile-content>
                </v-list-tile>
                <v-list-tile>
                  <v-list-tile-content>{{t('Saved places:')}}</v-list-tile-content>
                  <v-list-tile-content class="align-end">{{t('yes')}}</v-list-tile-content>
                </v-list-tile>
                <v-list-tile>
                  <v-list-tile-content>{{t('Notifications:')}}</v-list-tile-content>
                  <v-list-tile-content class="align-end">{{t('Yes')}}</v-list-tile-content>
                </v-list-tile>
                <v-list-tile>
                  <v-list-tile-content>{{t('Statistics:')}}</v-list-tile-content>
                  <v-list-tile-content class="align-end">{{t('Yes')}}</v-list-tile-content>
                </v-list-tile>
                <v-list-tile>
                  <v-list-tile-content>{{t('Price:')}}</v-list-tile-content>
                  <v-list-tile-content class="align-end">{{t('1$ per month')}}</v-list-tile-content>
                </v-list-tile>
                <v-card-actions class="justify-center">
                  <v-btn color="success" text-color="white" @click="handleTypeSelect($options.MONTH_1)">
                    {{t('Select')}}
                  </v-btn>
                </v-card-actions>
              </v-list>
            </v-card>

          </v-flex>
        </v-layout>
      </v-stepper-content>

      <v-stepper-content step="2">
        <vuetify-credit-card v-model="cardDetail" @submit="sendPayment"></vuetify-credit-card>
        <div class="mt-5"></div>
      </v-stepper-content>

    </v-stepper-items>
  </v-stepper>
</template>
<script>
import VuetifyCreditCard from '../../components/accounts/CreditCard'
import BasicClientApi from './basicApi'

const [MONTH_12, MONTH_1] = ['MONTH_12', 'MONTH_1']

let defaultProps = {
  number: '4532117080573700',
  name: 'Comprador T Cielo',
  expiry: '12/2018',
  cvc: '123'
}
export default {
  name: 'SubscribePremium',
  components: { VuetifyCreditCard },
  data () {
    return {
      step: 1,
      type: null,
      cardDetail: defaultProps

    }
  },
  created () {
    this.$options.MONTH_12 = MONTH_12
    this.$options.MONTH_1 = MONTH_1
  },
  methods: {
    handleTypeSelect (type) {
      this.step = 2
      this.type = type
    },
    sendPayment () {
      BasicClientApi.validatePayment()
        .then(response => {
          BasicClientApi.makeClientPremium({ 'token': response.data.token })
            .then(response => {
              this.setIsPremium(true)
              this.$router.push({ 'name': 'client-dashboard' })
            })
        })
    }
  }
}
</script>

<style scoped>

</style>
