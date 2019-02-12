<template>
  <device-statistics :id="id" :statistics="statistics"></device-statistics>
</template>

<script>
import AdminApi from './api'
import DeviceStatistics from '../../components/devices/Statistics'

export default {
  name: 'ClientDeviceStatistics',
  components: { DeviceStatistics },
  props: ['id'],
  data () {
    return {
      statistics: null
    }
  },
  created () {
    AdminApi.getDeviceStatistics({ id: this.id })
      .then(response => {
        this.statistics = response.data
      })
  }
}
</script>

<style scoped>

</style>
