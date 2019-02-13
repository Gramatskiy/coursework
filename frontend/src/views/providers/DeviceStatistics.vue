<template>
  <device-statistics :id="id" :statistics="statistics"></device-statistics>
</template>

<script>
import PremiumClientApi from './premiumApi'
import DeviceStatistics from '../../components/devices/Statistics'

export default {
  name: 'ClientDeviceStatistics',
  components: { DeviceStatistics },
  props: ['id'],
  data () {
    return {
      statistics: null,
      interval: null
    }
  },
  created () {
    this.interval = setInterval(() => PremiumClientApi.getDeviceStatistics({ id: this.id })
      .then(response => {
        this.statistics = response.data
      }), 1000)
  },
  destroyed () {
    clearInterval(this.interval)
  }
}
</script>

<style scoped>

</style>
