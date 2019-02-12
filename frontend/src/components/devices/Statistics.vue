<template>
  <div v-if="statistics">
    <h5 class="text-xs-center mt-3">{{t('Gap')}}</h5>
    <div>
      <v-radio-group v-model="gap.value" row class="justify-center">
        <v-radio v-for="option in gap.options" :key="option.value" :value="option"
                 :label="option.label"></v-radio>
      </v-radio-group>
    </div>
    <h5 class="text-xs-center">{{t('Measurements')}}</h5>
    <div class="d-flex row justify-end">
      <v-switch v-for="option in measurement.options" :key="option.value" v-model="measurement.value"
                :label="option.label" :value="option" class="pl-5"></v-switch>
    </div>
    <chart :chartData="prepareChartData" :options="{responsive: true, maintainAspectRatio: true}"
           :height="150"></chart>
  </div>
</template>

<script>
import Chart from './Chart'

const TEMPERATURE = { value: 'temperature', label: 'Temperature', color: 'rgba(153, 102, 255, 0.2)' }
const LAST_HOUR = { value: 'last_hour', label: 'Last hour', timeFormat: 'LTS' }
export default {
  name: 'DeviceStatistics',
  components: { Chart },
  props: ['id', 'statistics'],
  data () {
    return {

      gap: {
        value: LAST_HOUR,
        options: [
          LAST_HOUR,
          { value: 'last_day', label: 'Last day', timeFormat: 'LT' },
          { value: 'last_month', label: 'Last month', timeFormat: 'L' }
        ]
      },
      measurement: {
        value: [TEMPERATURE],
        options: [
          TEMPERATURE,
          { value: 'turbidity', 'label': 'Turbidity', color: 'rgba(255, 99, 132, 0.2)' },
          { value: 'ph_level', 'label': 'PH level', color: 'rgba(54, 162, 235, 0.2)' },
          { value: 'gyroscope', 'label': 'Gyroscope', color: 'rgba(255, 206, 86, 0.2)' },
          { value: 'accelerator', 'label': 'Accelerator', color: 'rgba(75, 192, 192, 0.2)' },
          { value: 'magnetometer', 'label': 'Magnometer', color: 'rgba(255, 159, 64, 0.2)' }
        ]
      }
    }
  },
  created () {
    this.$nextTick(() => {
      for (let item of this.gap.options) {
        item.label = this.$translate.text(item.label)
      }
      for (let item of this.measurement.options) {
        item.label = this.$translate.text(item.label)
      }
      this.title = this.$translate.text(this.title)
      console.log(this.$translate.locale)
    })
  },
  computed: {
    prepareChartData () {
      const indicators = this.statistics[this.gap.value.value]
      const labels = indicators.map(i => this.$moment(i.timestamp).format(this.gap.value.timeFormat))
      let datasets = []
      for (let option of this.measurement.value) {
        datasets.push({
          label: option.label,
          backgroundColor: option.color,
          data: indicators.map(i => i[option.value])
        })
      }
      return {
        labels,
        datasets
      }
    }
  }
}
</script>

<style scoped>

</style>
