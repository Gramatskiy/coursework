<template>
  <router-view/>
</template>

<script>

export default {
  name: 'App',
  mounted () {
    this.$translate.setLang('ua')
  }
}
</script>
