<template>
  <v-layout fill-height>
    <device-history :devices="devices" @deviceClicked="deviceClicked"></device-history>

    <v-flex class="fill-height" :class="selectedDevice ? 'xs12 md7' : 'xs12 md10'">
      <div class="group xs12">
        <GmapAutocomplete @place_changed="setPlace" placeholder="" required></GmapAutocomplete>
        <span class="highlight"></span>
        <span class="bar"></span>
        <label>Enter location</label>
      </div>
      <GmapMap
          :center="center"
          :zoom="zoom"
          map-type-id="terrain"
          class="map"
          @zoom_changed="_zoom => this.zoom = _zoom"
      >
        <GmapMarker
            :key="index"
            v-for="(device, index) in devices"
            :position="device.position"
            :icon="icon"
            :title="device.name"
            :clickable="true"
            @click="deviceClicked(device)"
        />
        <GmapMarker v-if="marker" key="marker" :position="marker.position" :title="marker.title"></GmapMarker>
      </GmapMap>
    </v-flex>
    <device-map-detail :device="selectedDevice"></device-map-detail>
  </v-layout>
</template>

<script>
import BasicClientApi from './basicApi'
import PremiumClientApi from './premiumApi'
import DeviceMapDetail from '../../components/devices/MapDetail'
import { mapGetters } from 'vuex'
import DeviceHistory from '../../components/devices/DeviceHistory'

export default {
  name: 'ClientMap',
  components: { DeviceHistory, DeviceMapDetail },
  data () {
    return {
      center: { lat: 10, lng: 10 },
      icon: {},
      zoom: 5,
      devices: [],
      selectedDevice: null,
      marker: null
    }
  },
  created () {
    this.$gmapApiPromiseLazy().then(response => {
      this.icon = {
        'scaledSize': new response.maps.Size(30, 30)
      }
    })
    navigator.geolocation.getCurrentPosition(location => {
      this.center = { lat: location.coords.latitude, lng: location.coords.longitude }
    })
    let promise
    if (this.$store.state.isPremium) {
      promise = PremiumClientApi.getDeviceList({})
    } else {
      promise = BasicClientApi.getDeviceList({})
    }
    promise
      .then(response => {
        for (let device of response.data) {
          if (device.measurements) {
            const lat = Number(device.measurements.lat)
            const lng = Number(device.measurements.lng)
            this.devices.push({ ...device, position: { lat, lng } })
          }
        }
      })
  },
  methods: {
    ...mapGetters(['isPremium']),
    deviceClicked (device) {
      this.center = device.position
      this.zoom = 7
      this.selectedDevice = device
    },
    setPlace (address) {
      const loc = address.geometry.location
      const position = { lat: loc.lat(), lng: loc.lng() }
      this.marker = { 'title': address.name, position }
      this.center = position
    }
  }
}
</script>

<style scoped lang="scss">
  .group {
    position: relative;
    height: 5%;
  }

  input {
    font-size: 18px;
    padding: 10px 10px 10px 5px;
    display: block;
    border: none;
    border-bottom: 1px solid #757575;
    width: 100%;
  }

  input:focus {
    outline: none;
  }

  label {
    color: #999;
    font-size: 18px;
    font-weight: normal;
    position: absolute;
    pointer-events: none;
    left: 5px;
    top: 10px;
    transition: 0.2s ease all;
    -moz-transition: 0.2s ease all;
    -webkit-transition: 0.2s ease all;
  }

  input:focus ~ label, input:valid ~ label {
    top: -20px;
    font-size: 14px;
    color: #5264AE;
  }

  .bar {
    position: relative;
    display: block;
    width: 100%;
  }

  .bar:before, .bar:after {
    content: '';
    height: 2px;
    width: 0;
    bottom: 1px;
    position: absolute;
    background: #5264AE;
    transition: 0.2s ease all;
    -moz-transition: 0.2s ease all;
    -webkit-transition: 0.2s ease all;
  }

  .bar:before {
    left: 50%;
  }

  .bar:after {
    right: 50%;
  }

  /* active state */
  input:focus ~ .bar:before, input:focus ~ .bar:after {
    width: 50%;
  }

  /* HIGHLIGHTER ================================== */
  .highlight {
    position: absolute;
    height: 60%;
    width: 100px;
    top: 25%;
    left: 0;
    pointer-events: none;
    opacity: 0.5;
  }

  /* active state */
  input:focus ~ .highlight {
    -webkit-animation: inputHighlighter 0.3s ease;
    -moz-animation: inputHighlighter 0.3s ease;
    animation: inputHighlighter 0.3s ease;
  }

  /* ANIMATIONS ================ */
  @-webkit-keyframes inputHighlighter {
    from {
      background: #5264AE;
    }
    to {
      width: 0;
      background: transparent;
    }
  }

  @-moz-keyframes inputHighlighter {
    from {
      background: #5264AE;
    }
    to {
      width: 0;
      background: transparent;
    }
  }

  @keyframes inputHighlighter {
    from {
      background: #5264AE;
    }
    to {
      width: 0;
      background: transparent;
    }
  }

  .map {
    width: 100%;
    height: 95%;
  }
</style>
